import pandas as pd
import matplotlib.pyplot as plt
import serial
import datetime

# Set up the serial connection
ser = serial.Serial('COM8', 9600, timeout=1)
ser.flush()

# DataFrame to store data
df = pd.DataFrame(columns=['Time', 'Temperature_C', 'Temperature_F', 'Voltage'])

# Function to convert milliseconds to HH:MM:SS format
def millis_to_time(millis):
    seconds = (millis // 1000) % 60
    minutes = (millis // (1000 * 60)) % 60
    hours = (millis // (1000 * 60 * 60)) % 24
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Continuously read from serial

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        data = line.split(',')
        print(data)

        if len(data) == 4:
            # Convert timestamp
            elapsed_ms = int(data[0])
            time_str = millis_to_time(elapsed_ms)

            tempC = float(data[1])
            tempF = float(data[2])
            turbidity = int(data[3])

            new_row = pd.DataFrame({'Time': [time_str], 'Temperature_C': [tempC], 'Temperature_F': [tempF], 'Turbidity': [turbidity]})
            df = pd.concat([df, new_row], ignore_index=True)

            if len(df) % 10 == 0:
                df.to_excel('sensor_data.xlsx', index=False)
