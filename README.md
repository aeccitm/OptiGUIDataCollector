#OptiGUI DataCollector
OptiGUI DataCollector is a Python 3.8 based graphical user interface that facilitates automated data collection in optics and photonics research and development equipment. It offers a user-friendly and intuitive platform for controlling a wide range of optical instruments, including spectrometers, and lasers. OptiGUI DataCollector's modular and flexible framework allows for easy integration with different types of devices. It simplifies experimental workflow and reduces human error by automating parameter control, data acquisition, and analysis. OptiGUI DataCollector is currently focused on optical mode conversion utilizing fiber optic technologies, but it may expand into other disciplines. It is beneficial for optical and photonics research due to its versatility and adaptability.

Steps for installation: XXXX

Dependencias:
OptiGUI DataCollector It is supported and tested on Python 3.8 and 3.10.

Main dependency is:

Minimum requirements:XXX

Software operation:
Before you can launch the OptiGUI DataCollector software, you need to have a Python compiler installed on your computer. You can choose any compiler that you prefer, such as IDLE, Visual Code Studio, Anaconda, PyCharm or Google Colab.
Once you have opened the Python compiler, you need to locate the Main_Interface.py module. This is the file that contains the code to launch the primary GUI interface. You can typically find this file in the folder where you have installed the OptiGUI DataCollector software.
Once you have located the Main_Interface.py module, you can open it by double-clicking on the file or using the file menu of your Python compiler. This will open the module in the editor window of the compiler.
To launch the code in the Main_Interface.py module, you need to click on the "Run" button or use the keyboard shortcut provided by your Python compiler. This will execute the code in the module and launch the primary GUI interface.
Once the primary GUI interface is launched, you can start exploring the different features and functionalities of the OptiGUI DataCollector software. You can set up experiments, collect data, visualize results, and export data using the different options provided in the GUI.
Equipos utilizados en la interfaz gráfica de usuario y tipos de conexión:
Below is a list of implementable hardware for the GUI. The developed modules are adaptable, allowing the researcher to attach his or her own equipment.
Three kinds of equipment protocols are implemented within the GUI's modules.
Ethernet data transfer
Serial communication
USB communication

Equipment
Manufacturer
Picture
Apex AP3352A and AP3350A Optical Tunable Laser Source Plug-in modules
APEX Technologies

PM-1600 -
High-speed power meter
EXFO


WiDy SWIR 640 - VGA Camera
New Imaging Technologies




Motorized Precision Rotation Mount
Thorlabs



T-Cube DC Servo Controller
Thorlabs






Arduino Mega 2560
Arduino AG




Ceramic heater



Thermistor







The user interface enables to conduct the following five distinct categories of research and developments:

Example #1: Reconstruction of transmission spectra
Here is a step-by-step guide to reconstruct transmission spectra using OptiGUI DataCollector:
Step 1: A drop-down menu will appear in the upper-right corner of the GUI, allowing you to select the reference laser source. Two PyApex tunable lasers are available for this example: Ref. AP3350A and Ref. AP3352A.
Step 2: Adjust the output power value of the tunable laser. The power range for these sources is between -30 dBm to +13 dBm.

Step 3: Establish the wavelength range based on the source of the reference laser. The wavelength range for Ref. AP3350A should be between 1527 and 1567 nm, and for Ref. AP3352A, it should be between 1567 and 1608 nm.
Step 4: Assign the wavelength step value. In this case, the tunable laser has a minimum wavelength step of 1 pm.
Step 5: Turn on the power meter by pressing the button that is situated at the very top of the user interface, and then enter exactly the same values for the wavelength range that were established earlier in the optical Light source (see Step 3).
Step 6: To begin running the software, click the PLAY button on the toolbar. The process of collecting data will now begin, and the transmission spectra will be reconstructed depending on the parameters that have been chosen.
Figure 1 illustrates the actions that the user must take when working within the viewing window in order to reconstruct the transmission spectra.

Figure 1. Step by step to reconstruct the transmission spectra using OptiGUI DataCollector.
When the GUI execution is finished, the transmission spectrum of the optical fiber device for the given wavelength range will be presented. Thus, the user will be able to view the transmission spectrum as depicted in Figure 2 via the software interface.
In addition to displaying the transmission spectra for the assigned wavelength range, the GUI also allows the user to save the acquired data as a .xlsx file for further analysis. This feature enables researchers to store and compare data from different experiments easily. 



Figura 2. Transmission spectrum displayed in the GUI.
Example #2: Measuring transmission spectra at different temperatures using an LPFG
Step 1: A drop-down menu will appear in the upper-right corner of the GUI, allowing you to select the reference laser source. Two PyApex tunable lasers are available for this example: Ref. AP3350A and Ref. AP3352A.
Step 2: The user has to adjust the tunable laser's output power value within the allowable range of -30 dBm to +13 dBm.
Step 3: Establish the wavelength range based on the source of the reference laser. The wavelength range for Ref. AP3350A should be between 1527 and 1567 nm, and for Ref. AP3352A, it should be between 1567 and 1608 nm.
Step 4: Assign the wavelength step value. In this case, the tunable laser has a minimum wavelength step of 1 pm.
Step 5: Turn on the power meter by pressing the button that is situated at the very top of the user interface, and then enter exactly the same values for the wavelength range that were established earlier in the optical Light source (see Step 3).
Step 6: The user must activate the temperature control, which is found in the lower left corner of the GUI. Following that, the user must assign the proper temperature range based on the experiment. This module could work at temperatures ranging from ambient temperature to 170 ºC.
Step 7: The user is responsible for assigning the proper temperature step, keeping in mind that the resolution of the thermistor being utilized is restricted to a maximum of 0.3ºC.
Step 8: Finally, the user will need to click on the PLAY button in order to begin the process of executing the program and receiving the transmission spectra that correspond to the chosen temperature and wavelength range.
A graphical illustration of the sequence of steps involved in the reconstruction of transmission spectra at different temperatures is provided in Figure 3. 

Figura 3. Step by step to reconstruct the transmission spectra at different temperatures using OptiGUI DataCollector.

Example #3: Capturing images by adjusting the wavelength of a tunable laser.
Step 1: A drop-down menu will appear in the upper-right corner of the GUI, allowing you to select the reference laser source. Two PyApex tunable lasers are available for this example: Ref. AP3350A and Ref. AP3352A.
Step 2: The user has to adjust the tunable laser's output power value within the allowable range of -30 dBm to +13 dBm.
Step 3: Establish the wavelength range based on the source of the reference laser. The wavelength range for Ref. AP3350A should be between 1527 and 1567 nm, and for Ref. AP3352A, it should be between 1567 and 1608 nm.
Step 4: Assign the wavelength step value. In this case, the tunable laser has a minimum wavelength step of 1 pm.
Step 5. To activate the camera, locate and select the button at the top of the Graphical User Interface (GUI). Once the camera is activated, it can be used to capture images. It is important to ensure that the camera is properly connected and configured before activation to ensure optimal performance. Additionally, it is recommended to refer to the user manual or instructions provided by the manufacturer for detailed guidance on the use of the camera and the associated features.
Step 6.  Click on PLAY to run the program. Thus, OptiGUI DataCollector will begin capturing images as the laser's operating wavelength varies.
Figure 4 displays the steps in the display window for capturing images at different wavelengths of the tunable laser. During the execution of the GUI, a new display window will be generated, which will show the captured image at the output of the optical fiber for the assigned wavelength. 

Figura 4. Step by step to capture images by adjusting the wavelength of a tunable laser using OptiGUI DataCollector.


Example #4:Capturing imaging by adjusting the polarization of light at the output of the optical fiber mode converter 
Step 1: A drop-down menu will appear in the upper-right corner of the GUI, allowing you to select the reference laser source. Two PyApex tunable lasers are available for this example: Ref. AP3350A and Ref. AP3352A.
Step 2: The user has to adjust the tunable laser's output power value within the allowable range of -30 dBm to +13 dBm.
Step 3: Establish the wavelength range based on the source of the reference laser. The wavelength range for Ref. AP3350A should be between 1527 and 1567 nm, and for Ref. AP3352A, it should be between 1567 and 1608 nm.
Step 4: Assign the wavelength step value. In this case, the tunable laser has a minimum wavelength step of 1 pm.
Step 5. To activate the camera, locate and select the button at the top of the Graphical User Interface (GUI). Once the camera is activated, it can be used to capture images. It is important to ensure that the camera is properly connected and configured before activation to ensure optimal performance. Additionally, it is recommended to refer to the user manual or instructions provided by the manufacturer for detailed guidance on the use of the camera and the associated features.
Step 6. The rotational base must be activated by the user; this button is placed on the left side of the GUI.
Step 7. The initial angle, the last angle, and the pitch in degrees should each be assigned to the rotational station. It is highly recommended that users look at the specifications provided by the manufacturer to know the resolution of this device.
Step 8. The rotation direction can either be clockwise or counterclockwise.
Step 9.  Click on the PLAY button to execute the program.

Figure 5 displays the steps in the GUI for capturing imaging by adjusting the polarization of light at the output of the optical fiber mode converter. During the execution of the GUI, a new display window will be generated, which will show the captured image at the output of the optical fiber for the assigned wavelength.


Figura 5. Step by step to capture images by adjusting by adjusting the polarization of light at the output of the optical fiber mode converter using OptiGUI DataCollector.


Example #5: Capturing imaging at different temperatures
Step 1: A drop-down menu will appear in the upper-right corner of the GUI, allowing you to select the reference laser source. Two PyApex tunable lasers are available for this example: Ref. AP3350A and Ref. AP3352A.
Step 2: The user has to adjust the tunable laser's output power value within the allowable range of -30 dBm to +13 dBm.
Step 3: Establish the wavelength range based on the source of the reference laser. The wavelength range for Ref. AP3350A should be between 1527 and 1567 nm, and for Ref. AP3352A, it should be between 1567 and 1608 nm.
Step 4: Assign the wavelength step value. In this case, the tunable laser has a minimum wavelength step of 1 pm.
Step 5. To activate the camera, locate and select the button at the top of the Graphical User Interface (GUI). Once the camera is activated, it can be used to capture images. It is important to ensure that the camera is properly connected and configured before activation to ensure optimal performance. Additionally, it is recommended to refer to the user manual or instructions provided by the manufacturer for detailed guidance on the use of the camera and the associated features.
Step 6: The user must activate the temperature control, which is found in the lower left corner of the GUI. Following that, the user must assign the proper temperature range based on the experiment. This module could work at temperatures ranging from ambient temperature to 170 ºC.
Step 7: The user is responsible for assigning the proper temperature step, keeping in mind that the resolution of the thermistor being utilized is restricted to a maximum of 0.3ºC.
Step 8.  Click on the PLAY button to execute the program.
Figure 6 depicts the steps in the display window for taking images of modes at the optical fiber's output under various temperature scenarios. During the execution of the GUI, a new display window will be generated, which will show the captured image at the output of the optical fiber for the assigned wavelength. 


Figura 6. Step by step to capture images at different temperatures using OptiGUI DataCollector.
