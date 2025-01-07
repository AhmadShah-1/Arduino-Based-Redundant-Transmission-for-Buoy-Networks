import serial
import datetime
import pandas as pd
import time
import os  # Import the os module to handle directories

# Set up the serial connection (adjust the COM port and baud rate as needed)
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

data = []  # List to store the parsed data
data_limit = 10  # Number of entries to collect before saving to Excel
max_entries = 100  # Stop after collecting 100 data points
start_time = time.time()  # Record the start time

# Get the current working directory (where the script is located)
save_directory = os.path.dirname(os.path.realpath(__file__))  # Ensure files are saved in the script's directory

try:
    while len(data) < max_entries:  # Stop after collecting 100 entries
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
            # Parsing the data
            parts = line.split(',')

            if len(parts) == 4:  # Adjusted for the addition of current measurement
                temp_data = parts[0].split(':')[1].replace('C', '')
                voltage_data = parts[1].split(':')[1]
                current_data = parts[2].split(':')[1]  # Extract current measurement
                time_data = parts[3].split(':')[1]

                days = int(time_data.split('d')[0])
                hours = int(time_data.split('d')[1].split('h')[0])
                mins = int(time_data.split('h')[1].split('m')[0])
                secs = int(time_data.split('m')[1])  # Removed .replace('s', '')

                total_seconds = days * 86400 + hours * 3600 + mins * 60 + secs

                # Calculate elapsed time
                elapsed_time = time.time() - start_time

                # Append data to the list
                data.append([time_data, float(temp_data), float(voltage_data), float(current_data), elapsed_time])

                # For testing, print the parsed data
                print(f"Time: {time_data}, Temp: {temp_data}, Voltage: {voltage_data}, Current: {current_data}, Elapsed Time: {elapsed_time:.2f} seconds")

                # Save to Excel every 10 entries
                if len(data) % data_limit == 0:
                    # Create a DataFrame
                    df = pd.DataFrame(data, columns=['Time', 'Temp', 'Voltage', 'Current', 'Elapsed Time'])
                    
                    # Create a file path in the same directory as the script
                    file_path = os.path.join(save_directory, 'sensor_data7cm_4hz_third.xlsx')
                    
                    # Save the DataFrame to Excel
                    df.to_excel(file_path, index=False)
                    print(f"Data saved to {file_path}")

except KeyboardInterrupt:
    print("Data collection stopped by user")
finally:
    # Save any remaining data to Excel before exiting
    if data:
        df = pd.DataFrame(data, columns=['Time', 'Temp', 'Voltage', 'Current', 'Elapsed Time'])
        
        # Create the file path again to save final data
        file_path = os.path.join(save_directory, 'sensor_data7cm_4hz_third.xlsx')
        
        df.to_excel(file_path, index=False)
        print(f"Final data saved to {file_path}")

    ser.close()  # Close the serial connection
    print("Program ended")
