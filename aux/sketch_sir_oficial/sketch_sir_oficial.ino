int led = 13;
char leituraSerial;
int sensorPin = A0;
int leituraSensor;
int LM35 = A0;
float temperatura;

void setup(){
  Serial.begin(9600);
}

void loop(){
  leituraSensor = analogRead(sensorPin);
  leituraSensor = map(leituraSensor,0,1023,0,255);
  
  temperatura = (float(analogRead(LM35))*5/(1023))/0.01;
  
  if(Serial.available() > 0){
  leituraSerial = Serial.read();  
  
  if(leituraSerial == '1'){
    digitalWrite(led,HIGH);
  }else if(leituraSerial == '2'){
    digitalWrite(led,LOW);
  }else if(leituraSerial == 't'){
    
    Serial.print("LUMINOSIDADE: ");
    Serial.print(leituraSensor);
    Serial.print("TEMPERATURA");
    Serial.println(temperatura);
  }
  
  
}}
