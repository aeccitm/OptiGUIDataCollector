import PyApex.AP1000 as AP1000
import autolv
import time


class Laser:
    
    def __init__(self, Box_module, potencia_in):
        self.Wavelength_list = []  #List for adding Wavelength values
        self.MyAP1000 = AP1000("192.168.1.1", PortNumber=5900, Simulation=False)
        self.seleccion = Box_module 
        self.MyTLS = self.MyAP1000.TunableLaser(self.seleccion + 1)  
        self.MyTLS.SetUnit("dBm")  #Laser Power Units
        self.MyTLS.SetPower(potencia_in)  #Laser output power
        
        
    def Wavelength_laser(self,Wavelength):
        self.MyTLS.SetWavelength(Wavelength) #Tell the laser to stop at that wavelength value.
        self.MyTLS.On()

if "__main__" == __name__:
    pass
