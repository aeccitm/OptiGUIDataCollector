import thorlabs_apt as apt

class Rotacional:
    def __init__(self, comboBox):
        self.motor = apt.Motor(83849132)
        self.sentido = comboBox


    def start(self,an):
        apt.list_available_devices()
        
        if self.sentido == 1:
             self.motor.move_by(an,blocking = True)
        else:
             self.motor.move_by(-1*an,blocking = True)
        rotacion = round(self.motor.position,an)
        print(rotacion)


if "__main__" == __name__:
    pass


