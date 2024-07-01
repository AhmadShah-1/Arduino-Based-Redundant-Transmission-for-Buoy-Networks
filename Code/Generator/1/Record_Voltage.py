

import serial
import csv
import time

# Specify your serial port and baud rate
serial_port = 'COM8'  # Change this to your serial port (on Windows it's COMx, on Unix-based it's typically /dev/ttyUSBx or /dev/ttyACMx)
baud_rate = 9600  # Adjust this according to your Arduino's Serial.begin rate

# Connect to the serial port
ser = serial.Serial(serial_port, baud_rate)

# Start time of the script
start_time = time.time()

# Define the CSV file where data will be saved
with open('C:/Users/ahmad/Desktop/OceanicProject/Code/Generator/1/voltage_data2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header of the CSV file
    writer.writerow(['Time (mm:ss)', 'Voltage'])

    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            print(line)
            # Calculate elapsed time since the script started 
            elapsed_time = time.time() - start_time
            # Convert elapsed time to minutes and seconds
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            # Format timestamp as mm:ss
            timestamp = f"{minutes:02}:{seconds:02}"
            # Write timestamp and voltage to CSV
            writer.writerow([timestamp, line])
            print(f"Logged at {timestamp}: {line} V")

    except KeyboardInterrupt:
        print("Logging stopped by user.")
        ser.close()  # Close serial port connection
