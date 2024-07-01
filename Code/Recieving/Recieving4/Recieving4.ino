#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN pins
const byte address[6] = "00001";

struct DataReceived {
  float tempC;
  float tempF;
  int turbidity;
  unsigned long elapsedTime;
};

DataReceived data;

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    radio.read(&data, sizeof(DataReceived));
    Serial.print(data.elapsedTime);
    Serial.print(",");
    Serial.print(data.tempC);
    Serial.print(",");
    Serial.print(data.tempF);
    Serial.print(",");
    Serial.println(data.turbidity);

  }
}
