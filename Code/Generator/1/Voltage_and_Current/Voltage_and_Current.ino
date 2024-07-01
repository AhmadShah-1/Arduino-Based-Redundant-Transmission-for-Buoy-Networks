// Constants
const int sensorIn = A0; // Sensor connected to A0
const float sensitivity = 185.0; // Sensitivity in mV/A (change this depending on your sensor's version, 100A = 66, 20A = 100, 5A = 185)
const float adcResolution = 1023.0; // ADC Resolution for Arduino (10-bit)

// Variables
float voltage = 0;
float current = 0;

void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud
}

void loop() {
  int sensorValue = analogRead(sensorIn); // Read the analog input
  voltage = (sensorValue / adcResolution) * 5; // Convert to voltage
  current = ((voltage - 2.5) / sensitivity) * 1000; // Convert voltage to current

  // Display Current on Serial Monitor
  Serial.print("Current: ");
  Serial.print(current); // Current in Amperes
  Serial.println(" A");

  delay(1000); // Delay for 1 second
}
