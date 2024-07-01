import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'processed_data.xlsx'  # Replace with your file path
data = pd.read_excel(file_path)

# Function to parse time components and convert to minutes
def parse_time_components(time_str):
    days, remainder = time_str.split('d')
    hours, remainder = remainder.split('h')
    minutes, seconds = remainder.split('m')
    seconds = seconds.replace('s', '')
    days, hours, minutes, seconds = map(int, [days, hours, minutes, seconds])
    return days, hours, minutes, seconds

def convert_to_minutes(time_str):
    days, hours, minutes, seconds = parse_time_components(time_str)
    return days * 24 * 60 + hours * 60 + minutes + seconds / 60

# Applying the conversion
data['TimeInMinutes'] = data['Time'].apply(convert_to_minutes)

# Adjusting the time so that the first data point starts at time zero
data['TimeInMinutes'] = data['TimeInMinutes'] - data['TimeInMinutes'].iloc[0]

# Creating the graphs
plt.figure(figsize=(15, 6))

# Temperature vs Time
plt.subplot(1, 2, 1)
plt.plot(data['TimeInMinutes'], data['Temperature'], marker='o', color='blue')
plt.title('Temperature vs Time')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')
plt.xticks(range(0, int(data['TimeInMinutes'].max()) + 1, 1))  # X-axis in increments of 1 minute
plt.grid(True)

# Turbidity vs Time
plt.subplot(1, 2, 2)
plt.plot(data['TimeInMinutes'], data['Turbidity'], marker='o', color='green')
plt.title('Turbidity vs Time')
plt.xlabel('Time (minutes)')
plt.ylabel('Turbidity')
plt.xticks(range(0, int(data['TimeInMinutes'].max()) + 1, 1))  # X-axis in increments of 1 minute
plt.grid(True)

plt.tight_layout()
plt.show()
