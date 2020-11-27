

const int buttonPin = 2;
const int ledPin = 3;
int buttonState = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() 
{
  int y1 = analogRead(A0);
  Serial.println(y1);
  
  buttonState = digitalRead(buttonPin);
    if (buttonState == LOW) 
    {
    digitalWrite(ledPin, LOW);
    } 
      else 
      {
      digitalWrite(ledPin, HIGH);
      }
  delay(500);

}
