#Here we are creating a wrapper for the NIT camera so that we can make calls to it to "capture" a frame and return the data as a numpy array

import camara.NITLibrary_x64_252_py38 as NITLibrary #Change xxx to match the version of NITLibrary you are using. Change ZZ to match the python version you are using
import numpy as np
import time
import threading 
import cv2

#from PIL import Image
import time
#import matplotlib.pyplot as plt
import os


class NITCam():

    def __init__(self):
        self.dev = None
        self.agc = None
        self.player = None
        self.nm = None
        self.myObserver = None
        self.images = []
        self.bitDepth=None

    def connectCam(self,setBitDepth=8):
        self.bitDepth=setBitDepth 
        '''If bitDepth=8: an AGC filter is added to the pipeline to convert incoming images to 8bit. If fixed conversion parameters are desired, switch to a NITManualGainControl filter
        bitDepth=14: images with no processing are provided'''
        self.nm = NITLibrary.NITManager.getInstance()
        self.dev = self.nm.openOneDevice()
        # If self.device is not open
        if (self.dev == None):
            print("No self.device Connected")
        else:
            self.dev.setParamValueOf("Exposure Time", 2000.0 )
            self.dev.updateConfig()

            if (
                    self.dev.connectorType() == NITLibrary.GIGE):  # To use self.agc camera must provide a RAW data; as Gige cameras can output different data types,
                # we force RAW output type
                print("GIGE CAM")
                self.dev.setParamValueOf("OutputType", "RAW").updateconfig()
            else:
                print("USB CAM")
                # Fps configuration: set fps to a mean value
            min_fps = self.dev.minFps()
            max_fps = self.dev.maxFps()
            self.dev.setFps(30)
            self.dev.updateConfig()

            self.mpo = myPyObserver()
            if self.bitDepth==8:
                self.myNuc = NITLibrary.NITToolBox.NITInterpolatedNuc(self.dev,'SN170531')
                self.myBPM = NITLibrary.NITToolBox.NITBPR(r'SN170531\NUC\25MHz\BPM.yml',640,512,0,0)
                self.myAGC = NITLibrary.NITToolBox.NITAutomaticGainControl() #Automatic gain control, allows to convert 14 bit images coming from the camera to 8 bit for displaying
                                                                             #For fixed conversion parameter change this to a NITManualGainControl
                self.dev << self.myNuc << self.myAGC << self.mpo
            elif self.bitDepth==14:
                self.myNuc = NITLibrary.NITToolBox.NITInterpolatedNuc(self.dev,'SN170531')
                self.myBPM = NITLibrary.NITToolBox.NITBPR(r'SN170531\NUC\25MHz\BPM.yml',640,512,0,0)
                self.myAGC = NITLibrary.NITToolBox.NITAutomaticGainControl()
                self.dev << self.myNuc << self.myAGC << self.mpo #Raw processing pipeline, outputs 14 bit images

            print("Device connected")
            #self.dev.start()
            #time.sleep(10)
            #self.dev.stop()

    def captureFrames(self, nbFrames=5):
        # Start Capture!!!
        self.dev.captureNFrames(nbFrames)
        self.dev.waitEndCapture()  # Wait end of capture
        self.images = self.mpo.images
        print(np.shape(self.images))
        return (self.images)

    def disconnect(self):
        # Don't forget Observers Diconnection
        #self.nm.reset()
        pass

class myPyObserver(NITLibrary.NITUserObserver):
    def __init__(self):
        NITLibrary.NITUserObserver.__init__(self)
        self.images = []
        self.counter=0
        print("init")

    def onNewFrame(self, array,info):  # You MUST define this function - It will be called on each frames
        # print("On new frame")
        new_frame = np.copy(array)
        self.images.append(new_frame)
        self.counter+=1
        print(self.counter, end="\r")

if __name__=="__main__":
    cam=NITCam()
    cam.connectCam()
    nbFrames=1
    nitFrame=cam.captureFrames(nbFrames)
    time.sleep(1)
    
    print(nitFrame)
    
    input("\n" +"Capture done, press enter to start processing images")
    # threshold=0.4
    for k in range(nbFrames):
        print(k,end="\r")
        img=nitFrame[k] 
        cv2.imshow("NITCamera",img)
        time.sleep(5)
        cv2.waitKey(50)
        time.sleep(5)
    cam.disconnect()

