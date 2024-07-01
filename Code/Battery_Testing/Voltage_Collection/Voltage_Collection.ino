// This is no longer relvant as we decided to use the arduino to record the data instead

#include <SD.h>

// Define analog input
#define ANALOG_IN_PIN A0

// Define SD card chip select pin
#define PIN_SPI_CS 4

// Floats for ADC voltage & Input voltage
float adc_voltage = 0.0;
float in_voltage = 0.0;

// Floats for resistor values in divider (in ohms)
float R1 = 30000.0;
float R2 = 7500.0; 

// Float for Reference Voltage
float ref_voltage = 5.0;

// Integer for ADC value
int adc_value = 0;

// File object for the SD card
File myFile;

void setup() {
  // Setup Serial Monitor
  Serial.begin(9600);

  // Initialize SD card
  if (!SD.begin(PIN_SPI_CS)) {
    Serial.println(F("SD CARD FAILED, OR NOT PRESENT!"));
    while (1); // don't do anything more:
  }
  Serial.println(F("SD CARD INITIALIZED."));

  // Open a new file in write mode
  char filename[] = "DATA00.TXT";
  for (uint8_t i = 0; i < 100; i++) {
    filename[4] = '0' + i/10;
    filename[5] = '0' + i%10;
    if (!SD.exists(filename)) {
      // if the file doesn't exist, create a new file
      break;
    }
  }
  myFile = SD.open(filename, FILE_WRITE);
  if (!myFile) {
    Serial.println(F("Error creating file on SD card"));
    return;
  }
  Serial.print(F("Logging data to: "));
  Serial.println(filename);
  myFile.println("Time (ms), Input Voltage");
}

void loop() {
  // Read the Analog Input
  adc_value = analogRead(ANALOG_IN_PIN);

  // Determine voltage at ADC input
  adc_voltage = (adc_value * ref_voltage) / 1024.0;

  // Calculate voltage at divider input
  in_voltage = adc_voltage * (R1 + R2) / R2;

  // Print results to Serial Monitor to 2 decimal places
  Serial.print("Input Voltage = ");
  Serial.println(in_voltage, 2);

  // Write data to SD card
  if (myFile) {
    myFile.print(millis());
    myFile.print(", ");
    myFile.println(in_voltage, 2);
    myFile.flush(); // Ensure data is written to the card
  } else {
    Serial.println("Error writing to file");
  }

  // Short delay
  delay(1200000);
}
