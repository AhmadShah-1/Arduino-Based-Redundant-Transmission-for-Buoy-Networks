import serial
import datetime
import pandas as pd
import time
import os  # Import the os module to handle directories

# ---- User Settings ----
COM_PORT = 'COM5'
BAUD_RATE = 9600
SHUNT_RESISTOR_OHMS = 1_800  
# -----------------------

# Set up the serial connection
ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Wait for the connection to establish

data = []          # List to store the parsed data
data_limit = 10    # Number of entries to collect before saving to Excel
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

            # Expecting 4 fields: Tc:..., V:..., I:..., T:...
            if len(parts) == 4:
                temp_data = parts[0].split(':')[1].replace('C', '')
                voltage_data = parts[1].split(':')[1]
                current_data = parts[2].split(':')[1]  # Extract current measurement
                time_data = parts[3].split(':')[1]

                # Parse the time string (e.g., "0d0h5m12")
                days = int(time_data.split('d')[0])
                hours = int(time_data.split('d')[1].split('h')[0])
                mins = int(time_data.split('h')[1].split('m')[0])
                secs = int(time_data.split('m')[1])

                total_seconds = days * 86400 + hours * 3600 + mins * 60 + secs

                # Calculate elapsed time since script started
                elapsed_time = time.time() - start_time

                # Convert the strings to floats
                float_temp = float(temp_data)
                float_voltage = float(voltage_data)
                float_current = float(current_data)

                # Calculate power = V^2 / R
                # If your resistor is 1.8kΩ, make sure SHUNT_RESISTOR_OHMS = 1800
                power = (float_voltage ** 2) / SHUNT_RESISTOR_OHMS

                # Append data to the list
                # [TimeString, Temp, Voltage, Current, Power, ElapsedTime]
                data.append([
                    time_data,
                    float_temp,
                    float_voltage,
                    float_current,
                    power,
                    elapsed_time
                ])

                # For testing, print the parsed data
                print(
                    f"Time: {time_data}, "
                    f"Temp: {float_temp}, "
                    f"Voltage: {float_voltage}, "
                    f"Current: {float_current}, "
                    f"Power: {power:.6f} W, "
                    f"Elapsed Time: {elapsed_time:.2f} s"
                )

                # Save to Excel every 10 entries
                if len(data) % data_limit == 0:
                    # Create a DataFrame
                    df = pd.DataFrame(
                        data,
                        columns=[
                            'Time', 
                            'Temp (°C)', 
                            'Voltage (V)', 
                            'Current (mA)', 
                            'Power (W)', 
                            'Elapsed Time (s)'
                        ]
                    )
                    
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
        df = pd.DataFrame(
            data,
            columns=[
                'Time', 
                'Temp (°C)', 
                'Voltage (V)', 
                'Current (mA)', 
                'Power (W)', 
                'Elapsed Time (s)'
            ]
        )

        # Create the file path again to save final data
        file_path = os.path.join(save_directory, 'sensor_data7cm_4hz_third.xlsx')
        
        df.to_excel(file_path, index=False)
        print(f"Final data saved to {file_path}")

    ser.close()  # Close the serial connection
    print("Program ended")
