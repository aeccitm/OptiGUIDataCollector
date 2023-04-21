import numpy as np
import time
from Tunable_Laser import Laser
from Degrees_polarization import Rotacional
import cv2
from Power_Meter import PowerMeter
from Image_Capture import captureImg
from Temperature_Control import Temperaturee
from Image_Display import ImageDisplay


class Ejecucion:
    def __init__(self,Box_module, Wavelength_1,Wavelength_2,resolution,potencia_in,
                 angle_1,angle_2,angle_3,comboBox,state_1,state_2,state_3,state_4,
                 temp1,temp2,deltatemp):
        self.power_list = 0
        self.waveleght_list=0
        self.final = False   
        self.Wavelength_1 = Wavelength_1
        self.Wavelength_2 = Wavelength_2
        self.resolution = resolution
        self.potencia_in = potencia_in
        self.angle_1 = angle_1
        self.angle_2 = angle_2
        self.angle_3 = angle_3
        self.laser = Laser(Box_module,potencia_in)
        self.direccion = comboBox
        self.camera = state_1
        self.rotacional = state_2
        self.temperatura = state_3
        self.power_meter = state_4
        self.temp1 = temp1
        self.temp2 = temp2
        self.deltatemp = deltatemp
        self.name = None   

    def start(self, ui):
        print("Starting program ...")
        if not self.camera:
            self.power = PowerMeter()
            if not self.temperatura:
                self.laser_power()
                
            else:
                self.controlTempe = Temperaturee()
                for t in np.arange(self.temp1, self.temp2 + self.deltatemp, self.deltatemp):
                    temp_Real = self.controlTempe.Start_Temperature(t)  #Temperature recorded by the terminstor
                    self.laser_power()
            self.final = True

        else:
            self.cameraa = captureImg()
            
            if not self.temperatura:
                if self.rotacional:
                    self.rotacional = Rotacional(self.direccion)
                    self.steps = np.insert(np.repeat(self.angle_3, self.angle_2/self.angle_3), 0, 0) #Assembles the angle step vector
                    self.anglee = list(range(0, self.angle_2 + 1, self.angle_3))
                    num = 0
                    for an in self.steps:
                        num = num + 1
                        self.laser_power()
                        self.rotacional.start(an)
                        time.sleep(2)
                        Img = np.array(self.cameraa.Capture())[-1,:,:] #Capture the image
                        self.name = './imagenes/ModeLP_' + str(self.Wavelength_1) + 'nm_' \
                            + str(self.anglee[num-1]) + '_degrees' + '.tiff'
                        cv2.imwrite(self.name, Img) #Save image
                        self.image = ImageDisplay(self.name)
                        self.image.display_image()
                    self.cameraa.disconect()    
                
                else:
                    for w in np.arange(self.Wavelength_1, self.Wavelength_2, self.resolution):
                        self.laser.Wavelength_laser(w)
                        self.laser.Wavelength_list.append(w) #Assembles the wavelength vector
                        time.sleep(2)
                        self.name = './imagenes/ModeLP_' + str(w) + 'nm' + '.tiff'
                        Img = np.array(self.cameraa.Capture())[-1,:,:] #Capture the image
                        cv2.imwrite(self.name, Img) #Save image
                        self.image = ImageDisplay(self.name)
                        self.image.display_image()
                self.cameraa.disconect()
                self.final = True    
                   
            else:
                self.controlTempe = Temperaturee()
                self.laser_power()
                
                for t in np.arange(self.temp1, self.temp2 + self.deltatemp, self.deltatemp):
                    temp_Real = self.controlTempe.Start_Temperature(t)
                    Img = np.array(self.cameraa.Capture())[-1,:,:]  #Capture the image
                    self.name = './imagenes/ModeLP_' + str(self.Wavelength_1) + 'nm_' + \
                             str(temp_Real) + 'C_' + '.tiff'
                    cv2.imwrite(self.name, Img)#Save image
                    self.controlTempe.Save()
                self.controlTempe.descoArduino()
                self.cameraa.disconect()

#______  Laser-Power_Meter operation  _______#            
    
    def laser_power(self):
        if self.Wavelength_1 == self.Wavelength_2:
            self.laser.Wavelength_laser(self.Wavelength_1)
            time.sleep(5)
            
        else:
             for w in np.arange(self.Wavelength_1, self.Wavelength_2, self.resolution):
                self.laser.Wavelength_laser(w)
                self.laser.Wavelength_list.append(w)  #Assembles the wavelength vector
                potencia_output = self.power.Wavelength_power(w)
                self.power.potencia.append(potencia_output.value)
             self.power_list = self.power.potencia
             self.waveleght_list = self.laser.Wavelength_list 
             self.final = True
   