import serial
import pandas as pd
import time

# Set up the serial connection (adjust the COM port and baud rate as needed)
ser = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

data = []  # List to store the parsed data
data_limit = 10  # Number of entries to collect before saving to Excel

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
            # Parsing the data
            parts = line.split(', ')

            print(parts)
            if len(parts) == 3:
                temp_data = parts[0].split(':')[1]
                turbidity_data = parts[1].split(':')[1]
                time_data = parts[2].split(':')[1]

                # Append data to the list
                data.append([time_data, float(temp_data), float(turbidity_data)])

                # For testing, print the parsed data
                print(f"Time: {time_data}, Temp: {temp_data}, Voltage: {turbidity_data}")

                # Save to Excel every 10 entries
                if len(data) >= data_limit:
                    # Create a DataFrame and save to Excel
                    df = pd.DataFrame(data, columns=['Time', 'Temp', 'Voltage'])
                    df.to_excel('sensor_data1.xlsx', index=False)

                    # Clear the data list
                    data = []

except KeyboardInterrupt:
    # Save any remaining data to Excel before exiting
    if data:
        df = pd.DataFrame(data, columns=['Time', 'Temp', 'Voltage'])
        df.to_excel('sensor_data1.xlsx', index=False)

    print("Data collection stopped")
finally:
    ser.close()  # Close the serial connection
