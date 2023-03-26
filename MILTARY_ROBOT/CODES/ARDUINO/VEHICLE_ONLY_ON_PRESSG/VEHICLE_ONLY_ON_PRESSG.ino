
char data;

void setup() {
  Serial.begin(9600);
  //pinMode(7,OUTPUT);
  //pinMode(LED_BUILTIN, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
}
  void loop() 
{  
  if(Serial.available()>0)
  {  
     delay(100);
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
}
