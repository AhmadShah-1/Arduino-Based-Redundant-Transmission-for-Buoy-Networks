import pandas as pd
import matplotlib.pyplot as plt

# Replace this with your CSV file path
csv_file = 'your_data.csv'

# Read the CSV file
data = pd.read_csv(csv_file)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(data['Time (Minutes)'], data['Voltage'], color='blue', marker='o')
plt.title('Voltage vs. Time')
plt.xlabel('Time (Minutes)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()
