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
float adc_voltage = 0.0;
float in_voltage = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;
float ref_voltage = 5.0;
int adc_value = 0;

RF24 radio(7, 8); // CE, CSN pins
const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);  // Initialize serial for debugging
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();

  sensors.begin();  // Start temperature sensor
}

void loop() {
  // Read voltage from sensor
  adc_value = analogRead(ANALOG_IN_PIN);
  adc_voltage = (adc_value * ref_voltage) / 1024.0;
  in_voltage = adc_voltage * (R1 + R2) / R2;

  // Read temperature
  sensors.requestTemperatures();
  float tempC = sensors.getTempCByIndex(0);

  // Elapsed time calculations
  unsigned long elapsedTime = millis();
  unsigned long days = elapsedTime / 86400000;
  unsigned long hours = (elapsedTime / 3600000) % 24;
  unsigned long mins = (elapsedTime / 60000) % 60;
  unsigned long secs = (elapsedTime / 1000) % 60;

  // Constructing the data string (ensuring it's concise)
  String dataString = "Tc:" + String(tempC, 1) +
                      ",V:" + String(in_voltage, 2) +
                      ",T:" + String(days) + "d" +
                      String(hours) + "h" + String(mins) + "m" + String(secs) + "s";

  // Converting String to C-string and ensuring it's null-terminated
  char dataToSend[32];
  dataString.toCharArray(dataToSend, sizeof(dataToSend));

  // Sending the data over nRF24L01
  radio.write(&dataToSend, sizeof(dataToSend));

  // Print to Serial Monitor for debugging
  Serial.println(dataToSend);

  delay(1000);  // Add delay to prevent flooding
}
