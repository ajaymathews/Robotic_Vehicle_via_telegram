const int mq3 = 3;
 
int limit;
int value;
 
void setup() 
{
  Serial.begin(9600);
}
 
void loop()
{
  value = analogRead(mq3); 
  Serial.print("Alcohol value: ");
  Serial.println(value);
  delay(1000);
}
