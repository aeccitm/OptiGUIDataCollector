import autolv
import time

class PowerMeter:  
    def __init__(self):
        self.Wavelength_list = []#List for adding Wavelength values
        self.potencia = [] #List for adding Power values
        self.lv = autolv.App()
        self.vi = self.lv.open('medidor.vi')  #Open LabVIEW file
      
        
    def Wavelength_power(self,Wavelength):
        self.vi.input = Wavelength #Tell the Power meter to stop at this wavelength value.
        self.vi.run()
        salida = self.vi.output #Measured power value
        time.sleep(5)
        return salida

if "__main__" == __name__:
    pass
