#include <AutoPID.h>
#include "InterpolationLib.h"

#define calefactor 10 //pin del calefactor
#define OUTPUT_MIN 0  //alternar inicio pid
#define OUTPUT_MAX 255 //alternar entre valor máximo el pid
#define KP 72 //valor del proporcional 
#define KI 0.0028544 //constante del integrador
#define KD 0 //constante del derivativo


//#define KP 70 //valor del proporcional 
//#define KI 1 //constante del integrador
//#define KD 80 //constante del derivativo

//variables
String input; 
int adc_in;
double t_[64] = {300, 295, 290, 285, 280, 275, 270, 265, 260, 255, 250, 245, 240, 235, 230, 225, 220, 215, 210, 205, 200, 195, 190, 185, 180, 175, 170, 165, 160, 155, 150, 145, 140, 135, 130, 125, 120, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15};
//array de datos de temperatura salida del pin T1 tomado del dataset para un sensor 
double adc_[64] = {23, 25, 27, 28, 31, 33, 35, 38, 41, 44, 48, 52, 56, 61, 66, 71, 78, 84, 92, 100, 109, 120, 131, 143, 156, 171, 187, 205, 224, 245, 268, 293, 320, 348, 379, 411, 445, 480, 516, 553, 591, 628, 665, 702, 737, 770, 801, 830, 857, 881, 903, 922, 939, 954, 966, 977, 985, 993, 999, 1004, 1008, 1012, 1016, 1020};
//array de datos de resistencia del pin t1 tomados del dataset
double temperature, setPoint = 0, outputVal;
unsigned long tiempo=0;
int contar_tiempo = 0, inicio = 0;

AutoPID myPID(&temperature, &setPoint, &outputVal, OUTPUT_MIN, OUTPUT_MAX, KP, KI, KD); //parametros libreria pid

//función que responde solo cuando se reciben datos de tipo serial 
void set() {
  if (Serial.available() > 0) {
    input = Serial.readStringUntil("\n");
    if (input.toFloat() == 0) {
      Serial.println(temperature);
    }
    else {
      setPoint = input.toFloat();
    }
    contar_tiempo = 0;
    inicio = millis();
  }
}

//configuración del setup para analisis del pin del calefactor y de la salida
void setup() {
  Serial.begin(9600);
  pinMode(calefactor, OUTPUT);


  myPID.setBangBang(20);
  myPID.setTimeStep(1);
}


void loop() {
  adc_in = analogRead(A14);//lectura del pin A14 del arduino que varía entre 0 y 5 voltios
  temperature = Interpolation::Linear(adc_, t_, 64, adc_in, false);//interpolación de los valores de temperatura relacionados con los valores de resistencia
  set();

  myPID.run(); //call every loop, updates automatically at certain time interval

  analogWrite(calefactor, outputVal);//lectura de salida en la pestaña de comando

//contar_tiempo comenzara al presionar enter con una temperatura deseada, avanzará el tiempo en milisegundos y retornará la temperatura,
//el setpoint y el tiempo transcurrido
  if (contar_tiempo == 1) {
    tiempo = millis() - inicio;
    Serial.print(temperature);
    Serial.print(",");
    Serial.print(setPoint);
    Serial.print(",");
    Serial.print(tiempo);
    Serial.println("");
    delay(500);
  }
  else {
    tiempo = millis() - inicio;
    Serial.print(temperature);
    Serial.print(",");
    Serial.print(setPoint);
    Serial.print(",");
    Serial.print(tiempo);
    Serial.println("");
    delay(500);
    //  Serial.println(((outputVal / 100) + setPoint - 0.5));
  }

}
