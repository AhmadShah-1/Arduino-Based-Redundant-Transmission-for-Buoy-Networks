import serial
import pandas as pd
from datetime import datetime
import time

# Setup the serial connection (Make sure the COM port and baud rate are correct)
# The COM port can be found in the Arduino IDE under Tools > Port
ser = serial.Serial('COM5', 9600, timeout=1)  # Replace 'COM_PORT' with your actual COM port

# Initialize a list to store the data as dictionaries
data = []

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode().strip()
        if line.startswith("Temperature:"):
            # Extract the temperature value from the line
            temperature = float(line.split(" ")[1])
            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(temperature)
            # Append the data as a dictionary to the list
            data.append({'Time': current_time, 'Temperature_C': temperature})
        time.sleep(1)  # Wait for a second before reading again

except KeyboardInterrupt:
    # When you press CTRL+C, the loop will break, and we proceed to save the data
    print("Saving data to Excel file...")
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    # Save the DataFrame to an Excel file
    df.to_excel('C:/Users/ahmad/Desktop/OceanicProject/Code/DataSurvey/Calibration/temperature_data.xlsx', index=False)
    print("Data saved!")
    ser.close()  # Close the serial port

except Exception as e:
    print("An error occurred:", e)
    ser.close()  # Close the serial port
