#include <Adafruit_Sensor.h>

int rele = 13;
char leituraSerial;
int sensorTemperatura = A0;
int leituraSensor;
int LM35 = A0;
float temperatura;
int estadoLed = 0;
void setup(){
  estadoLed = 0;
  Serial.begin(9600);
}

void loop(){
  leituraSensor = analogRead(sensorPin);
  leituraSensor = map(leituraSensor,0,1023,0,255);
  
  temperatura = (float(analogRead(LM35))*5/(1023))/0.01;
  
  digitalWrite(led,estadoLed);
  
  if(Serial.available() > 0){
  leituraSerial = Serial.read();  
  
  if(leituraSerial == '1'){
    estadoLed = 1;    
  }else if(leituraSerial == '2'){
    estadoLed = 0;   
  }else if(leituraSerial == 't'){
    
    Serial.print(temperatura);
    Serial.print(":");
    Serial.println(leituraSensor);
  }
  
  
}}
