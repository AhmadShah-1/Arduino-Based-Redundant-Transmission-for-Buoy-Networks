/* DS18B20 1-Wire digital temperature sensor with Arduino example code. More info: https://www.makerguides.com */

// Include the required Arduino libraries:
#include "OneWire.h"
#include "DallasTemperature.h"

// Define to which pin of the Arduino the 1-Wire bus is connected:
#define ONE_WIRE_BUS 2

// Create a new instance of the oneWire class to communicate with any OneWire device:
OneWire oneWire(ONE_WIRE_BUS);

// Pass the oneWire reference to DallasTemperature library:
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  // Send the command for all devices on the bus to perform a temperature conversion:
  sensors.requestTemperatures();

  float tempC = sensors.getTempCByIndex(0); // the index 0 refers to the first device
  float tempF = sensors.getTempFByIndex(0);

  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.print(" \xC2\xB0"); // shows degree symbol
  Serial.print("C  |  ");

  Serial.print(tempF);
  Serial.print(" \xC2\xB0");
  Serial.println("F");

  int sensorValue = analogRead(A0);
  Serial.print("Turbidity: ");
  Serial.println(sensorValue);

  delay(1000);
}
