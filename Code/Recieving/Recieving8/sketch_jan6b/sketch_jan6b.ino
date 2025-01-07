#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN - adjust these pins according to your hardware setup
const byte address[6] = "00001";

void setup() {
  Serial.begin(9600);  // Initialize serial communication for debugging
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();  // Start listening for data
}

void loop() {
  if (radio.available()) {
    char text[32] = "";  // 32-byte buffer to match the payload size from the transmitter
    radio.read(&text, sizeof(text));  // Read the incoming data into the buffer

    // Print the received data to the serial monitor
    Serial.println(text);

    // Optionally, parse the data if further processing is needed
    // Example: Splitting values using delimiters
  }
}
