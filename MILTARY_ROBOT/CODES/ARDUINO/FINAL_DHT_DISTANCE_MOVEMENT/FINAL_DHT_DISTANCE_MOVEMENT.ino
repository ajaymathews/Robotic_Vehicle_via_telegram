#include <SimpleDHT.h>
int pinDHT11 = 2;
const int trigPin = 9;
const int echoPin = 10;
long duration;
int distance;
char data;

SimpleDHT11 dht11(pinDHT11);

void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);
}

void loop() {

   if(Serial.available()>0)
  {  
     data=Serial.read();
     Serial.print(data);
      if(data=='W')
     {
      while(data=='W')
      {
       digitalWrite(5, HIGH);//MOVES FORWARD
       digitalWrite(6, LOW);

       digitalWrite(7, HIGH);
       digitalWrite(8, LOW);
 
       delay(250);
       break;
      }

     }
      if(data=='S')
      {
        while(data=='S')
      {  
       digitalWrite(5, LOW);//MOVES BACKWARD
       digitalWrite(6, HIGH);
       
       digitalWrite(7, LOW);
       digitalWrite(8, HIGH);
 
       delay(250);
       break;
      }
      }
       if(data=='D')
     {
      while(data=='D')
      {
       digitalWrite(6, HIGH);//TURNS RIGHT
       digitalWrite(5, LOW);
       
       digitalWrite(7, HIGH);
       digitalWrite(8, LOW);
 
       delay(250);
       break;
     }
     }
      if(data=='A')
     {
      while(data=='A')
      {
       digitalWrite(6, LOW);//TURNS LEFT
       digitalWrite(5, HIGH);
       
       digitalWrite(7, LOW);
       digitalWrite(8, HIGH);
 
       delay(250);
       break;
     }
     }
      if(data=='H')
     {
       digitalWrite(5, HIGH);//STOPS
       digitalWrite(6, HIGH);
       
       digitalWrite(7, HIGH);
       digitalWrite(8, HIGH);
     }
     else
     {
      digitalWrite(5, HIGH);//STOPS
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
 
     }
}
  
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance= duration*0.034/2;
Serial.print("Distance: ");
Serial.println(distance);

  
  Serial.println("Sample DHT11...");
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    Serial.print("Read DHT11 failed, err="); 
    Serial.println(err);
    delay(1000);
    return;
  }
  Serial.print("Sample OK: ");
  Serial.print((int)temperature); 
  Serial.print(" *C, "); 
  Serial.print((int)humidity); 
  Serial.println(" H");
  delay(1500);
}
 
