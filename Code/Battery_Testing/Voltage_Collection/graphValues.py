# C:/Users/ahmad/Desktop/OceanicProject/Code/Battery_Testing/Voltage_Collection/Merged_DATA.txt

import pandas as pd
import matplotlib.pyplot as plt

# Load the data, skipping the first row and parsing the two commas as delimiters
file_path = 'C:/Users/ahmad/Desktop/OceanicProject/Code/Battery_Testing/Voltage_Collection/Merged_DATA.txt'
data = pd.read_csv(file_path, skiprows=1, delimiter=',,', engine='python')
data.columns = ['Time (ms)', 'Input Voltage']

# Convert time from milliseconds to hours
data['Time (hours)'] = pd.to_numeric(data['Time (ms)']) / (3600 * 1000)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(data['Time (hours)'], data['Input Voltage'], label='Input Voltage', color='blue')
plt.xlabel('Time (hours)')
plt.ylabel('Voltage (V)')
plt.title('Input Voltage vs. Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
