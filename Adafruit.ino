const int buttonPin 2;
const int ledPin = 13;

int buttonState = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() 
{
  int y1 = analogRead(A0);
  Serial.println(y1);
  
  buttonState = digitalRead(buttonPin);
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH);
    } else 
      {
      digitalWrite(ledPin, LOW);
      }
  delay(2);

}
