from captureFrameStack import NITCam
import time
import os
import cv2
import numpy as np


class captureImg:
    def __init__(self):
        global cam
        cam = NITCam()
        cam.connectCam()
        self.rect1 = (89, 60, 510, 630)
        self.umbral_franjas = 120
        self.nitFrame = None
        

    def Capture(self):   
        self.nbFrames=1
        self.nitFrame = cam.captureFrames(self.nbFrames)
        time.sleep(1)
        self.verificador(self.nitFrame)
        return self.im_v_frame
    

    def verificador(self):
        files = [f for f in os.listdir(self.nitFrame) if f.endswith('.tiff')]
        for file_name in files:
            modosLP = os.path.join(self.nitFrame, file_name)
        im_ori = cv2.imread(modosLP)
        im = cv2.cvtColor(im_ori, cv2.COLOR_BGR2GRAY)
        self.im_v_frame = im[self.rect1[1]:self.rect1[1]+self.rect1[3], self.rect1[0]:self.rect1[0]+self.rect1[2]]

        # Aplicar el operador Canny para detectar los bordes
        umbral_minimo = 0.1  
        umbral_maximo = 0.9  

        bordes = cv2.Canny(self.im_v_frame, int(umbral_minimo*255), int(umbral_maximo*255))
        
        # Calcular la suma de los bordes en dirección vertical
        suma_vertical = np.sum(bordes, axis=0)
        
        # Contar el número de franjas horizontales detectadas
        num_franjas = np.count_nonzero(suma_vertical > 0)
        print(num_franjas)
        
        # Verificar si se deben eliminar las imágenes con múltiples franjas horizontales
        if num_franjas >= self.umbral_franjas:
            print("mala imagen")
            self.Capture()
        else:
            pass
    def disconect(self):
        cam.disconnect()

if __name__ == "__main__":
    pass