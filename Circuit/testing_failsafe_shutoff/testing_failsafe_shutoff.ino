void setup() {
  // Set pin 4 as an output
  pinMode(4, OUTPUT);
}

void loop() {
  // Turn pin 4 HIGH
  digitalWrite(4, HIGH);
  
  // Wait for 11 seconds (11000 milliseconds)
  delay(11000);
  
  // Turn pin 4 LOW2
  digitalWrite(4, LOW);

  delay(11000);

}
