void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available())
  {
    char h = Serial.read();
    if (h == 'g')
    {
      digitalWrite(13, HIGH); // Gate 1 LED and Buzzer
      Serial.write("GATE 1 OPENED");
    } 
    
    else if (h == 'l')
    {
      digitalWrite(13, LOW);
    }
    
    else if (h == 'e')
    {
      digitalWrite(13, HIGH);
      delay(500);
      digitalWrite(13, LOW);
      delay(500);
      digitalWrite(13, HIGH);
      Serial.write("GATE 2 CLOSED");
    }
  }
}
