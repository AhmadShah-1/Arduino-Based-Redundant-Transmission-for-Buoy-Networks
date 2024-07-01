#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CNS, CE - adjust these pins according to your hardware setup
const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}

void loop() {
  if (radio.available()) {
    char text[200] = ""; // Ensure this is large enough to hold your incoming data
    radio.read(&text, sizeof(text));
    Serial.println(text);    
  }
}
 