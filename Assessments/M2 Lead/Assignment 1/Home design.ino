// C++ code
//
void setup()
{
  pinMode(13, INPUT);
  Serial.begin(9600);
}

void loop()
{
  int p = digitalRead(13);
  if(p==1){
    digitalWrite(8, HIGH);
  }
  else{
    digitalWrite(8, LOW);
  }
  int Value_Gas = analogRead(A0);
  if (Value_Gas>=250){
    digitalWrite(4, HIGH);
  }
  else{
    digitalWrite(4, LOW);
  }
  
}