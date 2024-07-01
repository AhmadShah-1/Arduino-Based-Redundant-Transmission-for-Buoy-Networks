import serial
import time
import pandas as pd

# Set up the serial connection
ser = serial.Serial('COM10', 9600)
time.sleep(2)

data = []  # List to hold the data
save_interval = 120  # Save interval in seconds (2 minutes)
last_save_time = time.time()

# Function to save data to an Excel file
def save_to_excel(data_list):
    df = pd.DataFrame(data_list, columns=['Voltage', 'Timestamp'])
    df.to_excel('voltage_data.xlsx', index=False)

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            data.append([line, time.strftime("%Y-%m-%d %H:%M:%S")])
            current_time = time.time()
            # Check if 2 minutes have passed since last save
            if current_time - last_save_time >= save_interval:
                save_to_excel(data)
                data = []  # Reset the data list after saving
                last_save_time = current_time

except KeyboardInterrupt:
    # Save any remaining data when the script is stopped
    save_to_excel(data)
    ser.close()
    print("Data collection stopped and saved.")
