import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('C:/Users/ahmad/Desktop/OceanicProject/Code/Generator/1/voltage_data2.csv')

# Convert 'Time (mm:ss)' into a timedelta for plotting
data['Time (mm:ss)'] = pd.to_timedelta('00:' + data['Time (mm:ss)'])

# Plotting the data
plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(data['Time (mm:ss)'], data['Voltage'], label='Voltage (V)', color='b')  # Plot voltage vs. time
plt.xlabel('Time (mm:ss)')
plt.ylabel('Voltage (V)')
plt.title('Voltage over Time')
plt.grid(True)
plt.legend()

# Save the plot to a PNG file
plt.savefig('C:/Users/ahmad/Desktop/OceanicProject/Code/Generator/1/voltage_plot2.png')
plt.show()
