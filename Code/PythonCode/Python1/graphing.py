import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to convert HH:MM:SS to minutes
def convert_time_to_minutes(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 60 + int(m) + int(s) / 60

# Read data from Excel file
file_path = 'sensor_data.xlsx'  # Modify this if your file is in a different location
df = pd.read_excel(file_path)

# Check if the DataFrame is not empty
if not df.empty:
    # Convert Time from HH:MM:SS string to minutes
    df['Time'] = df['Time'].apply(convert_time_to_minutes)

    # Plot Temperature in a separate window
    plt.figure(figsize=(10, 5))
    plt.plot(df['Time'], df['Temperature_F'], label='Temp F')
    plt.xlabel('Time (Minutes)')
    plt.ylabel('Temperature')
    plt.title('Temperature Over Time')
    plt.legend()
    plt.show()

    # Plot Turbidity in a separate window
    plt.figure(figsize=(10, 5))
    plt.plot(df['Time'], df['Turbidity'], color='green', label='Turbidity')
    plt.xlabel('Time (Minutes)')
    plt.ylabel('Turbidity')
    plt.title('Turbidity Over Time')
    plt.legend()
    plt.show()

else:
    print("The DataFrame is empty. Check if the file path is correct and the file contains data.")
