#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include "OneWire.h"
#include "DallasTemperature.h"

// Temperature Sensor
#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Voltage Sensor
#define VOLTAGE_PIN A0
float adc_voltage = 0.0;
float in_voltage = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;
float ref_voltage = 5.0;
int adc_value = 0;

// Current Sensor
#define CURRENT_PIN A1
float adc_current_voltage = 0.0;
float current_mA = 0.0;
float shuntResistor = 1800.0; // Shunt resistor value in Ohms (1.8k)

// RF24 Setup
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
  adc_value = analogRead(VOLTAGE_PIN);
  adc_voltage = (adc_value * ref_voltage) / 1024.0;
  in_voltage = adc_voltage * (R1 + R2) / R2;

  // Read current from sensor
  int current_adc_value = analogRead(CURRENT_PIN);
  adc_current_voltage = (current_adc_value * ref_voltage) / 1024.0;
  current_mA = (adc_current_voltage / shuntResistor) * 1000.0; // Convert to mA

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
                      ",I:" + String(current_mA, 2) +
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
