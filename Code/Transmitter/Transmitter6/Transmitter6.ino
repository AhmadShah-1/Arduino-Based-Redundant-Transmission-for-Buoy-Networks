#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include "OneWire.h"
#include "DallasTemperature.h"

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Voltage Sensor
#define ANALOG_IN_PIN A0
// Floats for ADC voltage & Input voltage
float adc_voltage = 0.0;
float in_voltage = 0.0;

// Floats for resistor values in divider (in ohms)
float R1 = 30000.0;
float R2 = 7500.0; 

// Float for Reference Voltage
float ref_voltage = 5;

// Integer for ADC value
int adc_value = 0;


RF24 radio(7, 8); // CE, CSN pins
const byte address[6] = "00001";



void setup() {
  Serial.begin(9600);  // Add for debugging

  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void loop() {
  // VOLTAGE
  // Read the Analog Input
  adc_value = analogRead(ANALOG_IN_PIN);

  // Determine voltage at ADC input
  adc_voltage = (adc_value * ref_voltage) / 1024.0;

  // Calculate voltage at divider input
  in_voltage = adc_voltage * (R1 + R2) / R2;

  // TEMPERATURE
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);
  float tempF = sensors.getTempFByIndex(0);
  unsigned long elapsedTime = millis();

// Convert elapsed time to days, hours, minutes, and seconds
  unsigned long days = elapsedTime / 86400000; // 24 * 60 * 60 * 1000
  unsigned long hours = (elapsedTime / 3600000) % 24; // Convert to hours and get remainder after full days
  unsigned long mins = (elapsedTime / 60000) % 60; // Convert to minutes and get remainder after full hours
  unsigned long secs = (elapsedTime / 1000) % 60; // Convert to seconds and get remainder after full minutes

  String dataString = "";
  dataString += "Tc:" + String(tempC, 1);
  dataString += ", Voltage:" + String(in_voltage);
  dataString += ", Time:" + String(days) + "d" + String(hours) + "h" + String(mins) + "m" + String(secs) + "s";

  radio.write(dataString.c_str(), dataString.length());
  Serial.println(dataString);  // Debugging output

  // delay(500);
  
}
