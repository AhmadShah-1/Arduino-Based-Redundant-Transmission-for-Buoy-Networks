import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('sensor_data7cm.4hzthird.xlsx')

# Plot the data
plt.figure(figsize=(12, 6))

# Plot temperature over elapsed time
plt.subplot(2, 1, 1)
plt.plot(df['Elapsed Time'], df['Temp'], label='Temperature', color='red')
plt.xlabel('Elapsed Time (seconds)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature over Time Third Attempt')
plt.legend()

# Plot voltage over elapsed time
plt.subplot(2, 1, 2)
plt.plot(df['Elapsed Time'], df['Voltage'], label='Voltage', color='blue')
plt.xlabel('Elapsed Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Voltage over Time Third Attempt')
plt.legend()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
