#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include "OneWire.h"
#include "DallasTemperature.h"

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

RF24 radio(7, 8); // CE, CSN pins
const byte address[6] = "00001";

struct DataToSend {
  float tempC;
  float tempF;
  int turbidity;
  unsigned long elapsedTime;
};

DataToSend data;

void setup() {
  Serial.begin(9600);
  sensors.begin();

  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MAX);
  radio.stopListening();
}

void loop() {
  sensors.requestTemperatures();
  data.tempC = sensors.getTempCByIndex(0);
  data.tempF = sensors.getTempFByIndex(0);
  data.turbidity = analogRead(A0);
  data.elapsedTime = millis();

  for(int i = 0; i < 10; i++){
    radio.write(&data, sizeof(DataToSend));
    delay(10);
  }
}
