import serial
import datetime
import pandas as pd
import time

# Set up the serial connection (adjust the COM port and baud rate as needed)
ser = serial.Serial('COM9', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

data = []  # List to store the parsed data
data_limit = 10  # Number of entries to collect before saving to Excel
start_time = time.time()  # Record the start time

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
            # Parsing the data
            parts = line.split(', ')

            if len(parts) == 3:
                temp_data = parts[0].split(':')[1]
                turbidity_data = parts[1].split(':')[1]
                time_data = parts[2].split(':')[1]

                # Calculate elapsed time
                elapsed_time = time.time() - start_time

                # Append data to the list
                data.append([time_data, float(temp_data), float(turbidity_data), elapsed_time])

                # For testing, print the parsed data
                print(f"Time: {time_data}, Temp: {temp_data}, Voltage: {turbidity_data}, Elapsed Time: {elapsed_time:.2f} seconds")

                # Save to Excel every 10 entries
                if len(data) % data_limit == 0:
                    # Create a DataFrame and save to Excel
                    df = pd.DataFrame(data, columns=['Time', 'Temp', 'Voltage', 'Elapsed Time'])
                    df.to_excel('sensor_data7cm.4hzthird.xlsx', index=False)

except KeyboardInterrupt:
    print("Data collection stopped by user")
finally:
    # Save any remaining data to Excel before exiting
    if data:
        df = pd.DataFrame(data, columns=['Time', 'Temp', 'Voltage', 'Elapsed Time'])
        df.to_excel('sensor_data7cm.4hzthird.xlsx', index=False)

    ser.close()  # Close the serial connection
