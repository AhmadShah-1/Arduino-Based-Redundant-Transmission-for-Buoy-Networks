/* DS18B20 1-Wire digital temperature sensor with Arduino example code. More info: https://www.makerguides.com */

// Include the required Arduino libraries:
#include "OneWire.h"
#include "DallasTemperature.h"
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

// Define to which pin of the Arduino the 1-Wire bus is connected:
#define ONE_WIRE_BUS 2

// Create a new instance of the oneWire class to communicate with any OneWire device:
OneWire oneWire(ONE_WIRE_BUS);

// Pass the oneWire reference to DallasTemperature library:
DallasTemperature sensors(&oneWire);


RF24 radio(7, 8); // CE, CSN
const byte address[6] = "00001";


void setup() {
  // Begin serial communication at a baud rate of 9600:
  Serial.begin(9600);
  // Start up the library:
  sensors.begin();

  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void loop() {
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  int sensorValue = analogRead(A0);

  char text[32]; // Adjust the size as needed
  snprintf(text, sizeof(text), "%f %d", tempC, sensorValue);
  radio.write(&text, sizeof(text));

  delay(1000);
}




