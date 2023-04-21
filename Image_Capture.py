from captureFrameStack import NITCam
import time


class captureImg:
    def __init__(self):
        global cam
        cam = NITCam()
        cam.connectCam()

    def Capture(self):   
        self.nbFrames=1
        self.nitFrame = cam.captureFrames(self.nbFrames)
        self.data_dir = 'Users\Lab_optica\Desktop\Conexion de Equipos\imagenes'

        time.sleep(1)
        return self.nitFrame

    def disconect(self):
        cam.disconnect()

if __name__ == "__main__":
    pass

