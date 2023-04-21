from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import Execution
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        
###################__________________________________###########################
class Ui_MainWindow(object):
    def __init__(self):
        self.inicio = False
        self.camera = False
        self.ui = None
        self.gui = None
    def setupUi(self, MainWindow,ui):
        self.ui = ui
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 850)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setPixmap(QtGui.QPixmap("logo.png"))
        self.photo.setGeometry(20, 10, 350, 130)
        self.photo.setScaledContents(True)

      
        self.boton_ON = QtWidgets.QPushButton(self.centralwidget)
        self.boton_ON.setGeometry(QtCore.QRect(1150, 740, 140, 80))  
        self.boton_ON.setObjectName("boton_ON")
        self.boton_ON.setFont(QFont('Times', 12))
        self.boton_ON.setStyleSheet("background-color: #60E14C; border: 2px solid black;")
       
        self.boton_OFF = QtWidgets.QPushButton(self.centralwidget)
        self.boton_OFF.setGeometry(QtCore.QRect(1300, 740, 140, 80))
        self.boton_OFF.setObjectName("boton_OFF")
        self.boton_OFF.setFont(QFont('Times', 12))
        self.boton_OFF.setStyleSheet("background-color: #CA360E; border: 2px solid black;")


        #Laser module button
        self.Box_module = QtWidgets.QComboBox(self.centralwidget)
        self.Box_module.setGeometry(QtCore.QRect(1200, 90, 180, 65))
        self.Box_module.setObjectName("Box_module")
        self.Box_module.setFont(QFont('Times', 9))
        self.Box_module.addItem("")
        self.Box_module.addItem("")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 10, 35, 16))
        self.label_4.setObjectName("label_4")

        #Power button
        self.potencia_in = QtWidgets.QTextEdit(self.centralwidget)
        self.potencia_in.setGeometry(QtCore.QRect(1200, 220, 180, 65))
        self.potencia_in.setObjectName("potencia_in")
        self.potencia_in.setAlignment(QtCore.Qt.AlignCenter)
        self.potencia_in.setFont(QFont('Times', 12))
        self.potencia_in.setStyleSheet("border: 2px solid black;")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 120, 61, 21))
        self.label_7.setObjectName("label_7")

        #Initial wavelength
        self.Wavelength_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.Wavelength_1.setGeometry(QtCore.QRect(1200, 380, 180, 65))
        self.Wavelength_1.setObjectName("Wavelength_1")
        self.Wavelength_1.setStyleSheet("border: 2px solid black;")
        self.Wavelength_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Wavelength_1.setFont(QFont('Times', 12))

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1140, 390, 50, 50))
        self.label_15.setObjectName("label_15")
        
        #Title star wavelength
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1140, 390, 50, 50))
        self.label.setObjectName("label")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 190, 35, 10))
        self.label_5.setObjectName("label_5")

        #Final wavelength
        self.Wavelength_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Wavelength_2.setGeometry(QtCore.QRect(1200, 480, 180, 65))
        self.Wavelength_2.setObjectName("Wavelength_2")
        self.Wavelength_2.setStyleSheet("border: 2px solid black;")
        self.Wavelength_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Wavelength_2.setFont(QFont('Times', 12))

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(610, 230, 35, 16))
        self.label_8.setObjectName("label_8")

        #Resolution button
        self.resolucion = QtWidgets.QTextEdit(self.centralwidget)
        self.resolucion.setGeometry(QtCore.QRect(1200, 620, 180, 65))
        self.resolucion.setObjectName("resolucion")
        self.resolucion.setFont(QFont('Times', 12))
        self.resolucion.setAlignment(QtCore.Qt.AlignCenter)
        self.resolucion.setStyleSheet("border: 2px solid black;")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 260, 81, 20))
        self.label_6.setObjectName("label_6")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 220, 21, 21))
        self.label_2.setObjectName("label_2")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(520, 260, 81, 20))
        self.label_20.setObjectName("label_20")

    ######______ Small frame ______#####
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(380, 150, 720, 551))
        self.frame.setStyleSheet("border: 2px solid #000000")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

    ######______ Large frame ______#####
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 720, 551))
        self.frame_2.setStyleSheet("QFrame{\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "border:2px solid #000000;\n"
                                    "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("QLabel{\n"
                                 "border: none;\n"
                                 "}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.grafica = QtWidgets.QVBoxLayout()
        self.grafica.setObjectName("grafica")
        self.verticalLayout_3.addLayout(self.grafica)
        self.verticalLayout_3.setGeometry(QtCore.QRect(170, 170, 920, 951))
     
        #Initial angle
        self.angle_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.angle_1.setGeometry(QtCore.QRect(120, 280, 180, 65))
        self.angle_1.setObjectName("angle_1")
        self.angle_1.setFont(QFont('Times', 12))
        self.angle_1.setText("0")
        self.angle_1.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_1.setStyleSheet("border: 2px solid black;")
        self.angle_1.setDisabled(True)
        
        #End angle
        self.angle_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.angle_2.setGeometry(QtCore.QRect(120, 380, 180, 65))
        self.angle_2.setObjectName("angle_2")
        self.angle_2.setFont(QFont('Times', 12))
        self.angle_2.setText("0")
        self.angle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_2.setStyleSheet("border: 2px solid black;")
        self.angle_2.setDisabled(True)
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 140, 31, 21))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 380, 180, 65))
        self.label_10.setObjectName("label_10")
        
        #Angle step size
        self.angle_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.angle_3.setGeometry(QtCore.QRect(120, 480, 180, 65))
        self.angle_3.setObjectName("angle_3")
        self.angle_3.setFont(QFont('Times', 12))
        self.angle_3.setText("1")
        self.angle_3.setAlignment(QtCore.Qt.AlignCenter)
        self.angle_3.setStyleSheet("border: 2px solid black;")
        self.angle_3.setDisabled(True)
    
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 210, 31, 21))
        self.label_12.setObjectName("label_12")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 110, 81, 21))
        self.label_11.setObjectName("label_11")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1190, 340, 250, 30))
        self.label_13.setObjectName("label_13")

        #Rotation direction button
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 620, 220, 65))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QFont('Times', 10))
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(40, 250, 81, 21))
        self.label_14.setObjectName("label_14")
        

        #Initial temperature
        self.temp1 = QtWidgets.QTextEdit(self.centralwidget)
        self.temp1.setGeometry(QtCore.QRect(400, 740, 180, 65))
        self.temp1.setObjectName("temp1")
        self.temp1.setFont(QFont('Times', 12))
        self.temp1.setText("0")
        self.temp1.setAlignment(QtCore.Qt.AlignCenter)
        self.temp1.setStyleSheet("border: 2px solid black;")
        self.temp1.setDisabled(True)
        
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")

        #Final temperature
        self.temp2 = QtWidgets.QTextEdit(self.centralwidget)
        self.temp2.setGeometry(QtCore.QRect(630, 740, 180, 65))
        self.temp2.setObjectName("temp1")
        self.temp2.setFont(QFont('Times', 12))
        self.temp2.setText("0")
        self.temp2.setAlignment(QtCore.Qt.AlignCenter)
        self.temp2.setStyleSheet("border: 2px solid black;")
        self.temp2.setDisabled(True)

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(310, 340, 71, 21))
        self.label_18.setObjectName("label_1")
       
        #temperature step
        self.deltatemp = QtWidgets.QTextEdit(self.centralwidget)
        self.deltatemp.setGeometry(QtCore.QRect(860,740, 180, 65))
        self.deltatemp.setObjectName("deltatemp")
        self.deltatemp.setFont(QFont('Times', 12))
        self.deltatemp.setText("0")
        self.deltatemp.setAlignment(QtCore.Qt.AlignCenter)
        self.deltatemp.setStyleSheet("border: 2px solid black;")
        self.deltatemp.setDisabled(True)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 340, 61, 21))
        self.label_3.setObjectName("label_3")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(180, 340, 71, 21))
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(310, 340, 71, 21))
        self.label_17.setObjectName("label_17")

        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(310, 340, 71, 21))
        self.label_21.setObjectName("label_21")
        
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(310, 340, 71, 21))
        self.label_22.setObjectName("label_22")

        #ON/OFF Rotational 
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.setGeometry(QtCore.QRect(115, 100, 250, 200))
        self.checkBox1.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "width :40px;"
                               "height : 40px;"
                               "}")
        self.checkBox1.setObjectName("checkBox")
        self.checkBox1.setFont(QFont('Times', 12))

        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(350, 135, 71, 21))
        self.label_24.setObjectName("label_24")
        self.checkBox1.stateChanged.connect(self.clickBox_rotational)
       
        #OFF/ON Temperature
        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2.setGeometry(QtCore.QRect(100, 670, 280, 200))
        self.checkBox2.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "width :40px;"
                               "height : 40px;"
                               "}")
        self.checkBox2.setObjectName("checkBox")
        self.checkBox2.setFont(QFont('Times', 12))
        self.checkBox2.stateChanged.connect(self.clickBox_temp)

        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(350, 135, 71, 21))
        self.label_25.setObjectName("label_25")

        #OFF/ON Power meter
        self.checkBox3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox3.setGeometry(QtCore.QRect(800, 20, 280, 200))
        self.checkBox3.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "width :40px;"
                               "height : 40px;"
                               "}")
        self.checkBox3.setObjectName("checkBox")
        self.checkBox3.setFont(QFont('Times', 12))
        self.checkBox3.stateChanged.connect(self.clickBox_power)
        self.state_camera = False
        self.state_rotational = False
        self.state_power = False
        self.state_temp = False
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(350, 135, 71, 21))
        self.label_26.setObjectName("label_26")

        #OFF/ON Camera
        self.checkBox4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox4.setGeometry(QtCore.QRect(500, 20, 280, 200))
        self.checkBox4.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "width :40px;"
                               "height : 40px;"
                               "}")
        self.checkBox4.setObjectName("checkBox")
        self.checkBox4.setFont(QFont('Times', 12))
        self.checkBox4.stateChanged.connect(self.clickBox_camera)

        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(350, 135, 71, 21))
        self.label_27.setObjectName("label_18")

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(350, 340, 71, 21))
        self.label_19.setObjectName("label_19")
        
    # Start button for execution 
        self.boton_ON.clicked.connect(lambda: self.start() )
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 18))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def start(self):
        self.inicio = Execution.Ejecucion(self.Box_module.currentIndex(),
                                        int(self.Wavelength_1.toPlainText()), 
                                        int(self.Wavelength_2.toPlainText()), 
                                        float(self.resolucion.toPlainText()), 
                                        int(self.potencia_in.toPlainText()),
                                        int(self.angle_1.toPlainText()),
                                        int(self.angle_2.toPlainText()),
                                        int(self.angle_3.toPlainText()),
                                        self.comboBox.currentIndex(),
                                        self.state_camera,
                                        self.state_rotational,
                                        self.state_temp,
                                        self.state_power,
                                        float(self.temp1.toPlainText()),
                                        float(self.temp2.toPlainText()),
                                        float(self.deltatemp.toPlainText()))
        self.inicio.start(self.ui)
        self.plots(self.inicio.waveleght_list,self.inicio.power_list)
        
    
    def plots(self,waveleght_list, potencia_list):
                     
            sc = MplCanvas(self, width=15, height=30, dpi=100)
            sc.axes.plot(waveleght_list,potencia_list)
            self.grafica.addWidget(sc) 
            
    def image_label(self):
        print(self.inicio.name)

#---------------------       

    def clickBox_camera(self, state):
        if state == QtCore.Qt.Checked:
            self.camera = True
            print("Camera Enable")
            self.state_camera = True
        else:
            print("Camera Disabled")
            self.state_camera = False

    def clickBox_rotational(self,state):
        print("Rotational Enabled")
        if state == QtCore.Qt.Checked:
            self.state_rotational = True
            self.angle_1.setDisabled(False)
            self.angle_2.setDisabled(False)
            self.angle_3.setDisabled(False)
        else:
            self.state_rotational = False
            self.angle_1.setDisabled(True)
            self.angle_2.setDisabled(True)
            self.angle_3.setDisabled(True)
            print("Rotational Disabled")

    def clickBox_temp(self, state):
        if state == QtCore.Qt.Checked:
            self.state_temp = True
            self.deltatemp.setDisabled(False)
            self.temp1.setDisabled(False)
            self.temp2.setDisabled(False)
            print("Temperature enabled") 
        else:
            print("Temperature Disabled")
            self.state_temp = False
            self.deltatemp.setDisabled(True)
            self.temp1.setDisabled(True)
            self.temp2.setDisabled(True)

    def clickBox_power(self,state):
        if state == QtCore.Qt.Checked:
            self.state_power = True
            print("Power Meter enabled")
        else:
            self.state_power = False
            print("Power Meter disabled")
         
#----------------------         
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_ON.setText(_translate("MainWindow", "PLAY"))
        self.boton_OFF.setText(_translate("MainWindow", "STOP"))
        self.Box_module.setItemText(0, _translate("MainWindow", "Ref. AP3350A"))
        self.Box_module.setItemText(1, _translate("MainWindow", "Ref. AP3352A"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Laser source</span></p></body></html>"))
        self.label_4.setGeometry(QtCore.QRect(1220, 30, 160, 80))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Output power</span></p></body></html>"))
        self.label_7.setGeometry(QtCore.QRect(1218, 160, 160, 80))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">nm</span></p></body></html>"))
        self.label_5.setGeometry(QtCore.QRect(1399, 370, 160, 80))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Transmission Spectrum</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">nm</span></p></body></html>"))
        self.label_8.setGeometry(QtCore.QRect(1399, 470, 160, 80))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">nm</span></p></body></html>"))
        self.label_20.setGeometry(QtCore.QRect(1399, 610, 160, 80))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Steps</span></p></body></html>"))
        self.label_6.setGeometry(QtCore.QRect(1260, 560, 190, 80))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Start</span></p></body></html>"))
        self.label_15.setGeometry(QtCore.QRect(1140, 380, 160, 80))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">End</span></p></body></html>"))
        self.label_2.setGeometry(QtCore.QRect(1150, 480, 160, 80))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Start</span></p></body></html>"))
        self.label_9.setGeometry(QtCore.QRect(60, 270, 160, 80))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">End</span></p></body></html>"))
        self.label_10.setGeometry(QtCore.QRect(70, 370, 160, 80))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Steps</span></p></body></html>"))
        self.label_12.setGeometry(QtCore.QRect(50, 470, 160, 80))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Polarization angle </span></p></body></html>"))
        self.label_11.setGeometry(QtCore.QRect(120, 220, 190, 80))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Output Wavelength</span></p></body></html>"))
        self.label_13.setGeometry(QtCore.QRect(1185, 310, 280, 100))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Rotation Direction</span></p></body></html>"))
        self.label_14.setGeometry(QtCore.QRect(100, 560, 190, 80))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">°C</span></p></body></html>"))
        self.label_21.setGeometry(QtCore.QRect(815, 735, 160, 80))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">°C</span></p></body></html>"))
        self.label_22.setGeometry(QtCore.QRect(585, 735, 160, 80))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">°C</span></p></body></html>"))
        self.label_23.setGeometry(QtCore.QRect(1045, 735, 160, 80))
        self.comboBox.setItemText(0, _translate("MainWindow", "Clockwise"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Counterclockwise"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Initial Temp.</span></p></body></html>"))
        self.label_16.setGeometry(QtCore.QRect(427, 680, 160, 80))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Steps</span></p></body></html>"))
        self.label_17.setGeometry(QtCore.QRect(918, 680, 160, 80))
        self.checkBox1.setText(_translate("MainWindow", "Enable Rotational"))
        self.checkBox2.setText(_translate("MainWindow", "Enable Temperature"))
        self.checkBox3.setText(_translate("MainWindow", "Enable Power Meter"))
        self.checkBox4.setText(_translate("MainWindow", "Enable Camera"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">End Temp.</span></p></body></html>"))
        self.label_18.setGeometry(QtCore.QRect(659, 680, 160, 80))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">dBm</span></p></body></html>"))
        self.label_19.setGeometry(QtCore.QRect(1390, 210, 160, 80))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow,ui)
    MainWindow.show()
    sys.exit(app.exec_())
