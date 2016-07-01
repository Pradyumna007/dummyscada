int trig = 12;
int echo = 11;
void setup() 
{
  pinMode(echo, INPUT); 
  pinMode(trig, OUTPUT);
  pinMode(22, OUTPUT);
  pinMode(23, OUTPUT);
  pinMode(24, OUTPUT);
  pinMode(25, OUTPUT);
  pinMode(26, OUTPUT);
  pinMode(27, OUTPUT);
  pinMode(28, OUTPUT);
  pinMode(29, OUTPUT);
  Serial.begin(9600);
}

void loop()
{ 
  long t = 0, h = 0, l = 0 , v = 0;
  
  
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  
  t = pulseIn(echo, HIGH);
  
  h = t / 58;
 
  l = 40 - h;
  
  v = 100*50*l;

  delay(1000);
  
  
  while (Serial.available())
  {
    char h = Serial.read();
    
    if (h == 'g') // GATE 1
    {
      digitalWrite(22, HIGH);
      digitalWrite(23, HIGH);
      digitalWrite(24, LOW);
      Serial.write("Gate 1 Opened");
    }
    
    else if (h == 'l') // GATE 1
    {
      digitalWrite(22, LOW);
    }
    
    else if (h == 'e') // GATE 1
    {
      digitalWrite(22, HIGH);
      digitalWrite(24, HIGH);
      digitalWrite(23, LOW);
      Serial.write("Gate 1 Closed");
    }
    
    
    else if (h == 'z') // GATE 2
    {
      digitalWrite(25, HIGH);
      digitalWrite(26,HIGH);
      digitalWrite(27, LOW);
      Serial.write("Gate 2 Opened");
    }
    
    else if (h == 'n') // GATE 2
    {
      digitalWrite(25, LOW);
    }
    
    else if (h == 'f') // GATE 2
    {
      digitalWrite(25, HIGH);
      digitalWrite(27, HIGH);
      digitalWrite(26, LOW);
      Serial.write("Gate 2 Closed");
    }
    
    else if (h == 'b') // GATE 3
    {
      digitalWrite(28, HIGH);
      digitalWrite(29, HIGH);
      digitalWrite(30, LOW);
      Serial.write("Gate 3 Opened");
    }
    
    else if (h == 'o') // GATE 3
    {
      digitalWrite(28, LOW);
    }
    
    else if (h == 'j') // GATE 3
    {
      digitalWrite(28, HIGH);
      digitalWrite(30, HIGH);
      digitalWrite(29, LOW);
      Serial.write("Gate 3 Closed");
    }
    
    else if (h == 'v')
    {
      Serial.println(v);
    }
    
    else if (h = 'k')
    {
      Serial.println(k);
    }
  }
}
