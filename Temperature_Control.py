import serial
import time


class Temperaturee:

    def __init__(self):
#----------------------------------ARDUINO SERIAL PORT-------------------------------------
        self.mega = serial.Serial(port = 'COM3', baudrate = 115200, timeout = 1, write_timeout = 1)

#---------------------------------- Acquisition -----------------------------------------
    def Start_Temperature(self, tem): 

        t_est = 60    # Stabilization time [sec].
        umbral = 0.5  # Acceptable temperature threshold [°C].

        print('T_setpoint = ' + str(tem) + '°C')
        
        self.mega.write(str(tem).encode('utf-8')) #Send temperature setpoint to the arduino
        self.mega.reset_input_buffer()
        time.sleep(1)
        self.mega.write(str(tem).encode('utf-8')) #Send temperature setpoint to the arduino
        self.mega.reset_input_buffer()                     

        time.sleep(t_est) #Wait stabilization time (obtained experimentally)
        setpoint = False

        while setpoint == False:
            try:
                self.mega.write(str(tem).encode('utf-8'))  #Send temperature setpoint to the arduino
                self.mega.reset_input_buffer()  
                self.mega.flush()
                T = float(self.mega.readline().decode("utf-8")[0:-2])
                print(T)
            except:
                print("ERROR")
            # Difference between setpoint and actual temperature must be less than the threshold
            if abs(T-tem) < umbral:
                setpoint = True
        return T 
           
#--------- Guarda temperatura real --------------          
    def Save(self):
        self.mega.flush()
        T = float(self.mega.readline().decode("utf-8")[0:-2]) 
           
 #--------- Disconnect Arduino --------------     
    def descoArduino(self):
        self.mega.write(str(25).encode('utf-8'))  #Send temperature setpoint to the arduino
        self.mega.close()