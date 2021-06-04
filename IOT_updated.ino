#define BLYNK_PRINT Serial
#include<ESP8266WiFi.h>
#include<BlynkSimpleEsp8266.h>

char auth[]="Auth Token";
char ssid[]="Wifi Name";
char pass[]="Wifi Password";
int pin2=D1;
int pin3=D2;
int pin4=D3;
int pin5=D4;
void setup() {
    // put your setup code here, to run once:
   pinMode(pin2,OUTPUT);
   pinMode(pin3,OUTPUT);
   pinMode(pin4,OUTPUT);
   pinMode(pin5,OUTPUT);
  
   digitalWrite(pin2,HIGH);
   digitalWrite(pin3,HIGH);
   digitalWrite(pin4,HIGH);
   digitalWrite(pin5,HIGH);
  
   
    Serial.begin(9600); 
  Blynk.begin(auth,ssid,pass);
 
}
void loop() {
Blynk.run();
}
