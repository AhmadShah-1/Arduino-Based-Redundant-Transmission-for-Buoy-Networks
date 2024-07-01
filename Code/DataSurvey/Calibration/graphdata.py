import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

# Load the .xlsx file into a DataFrame
df = pd.read_excel('C:/Users/ahmad/Desktop/OceanicProject/Code/DataSurvey/Calibration/temperature_data.xlsx', engine='openpyxl')

# Ensure the 'Time' column is in the correct datetime format
df['Time'] = pd.to_datetime(df['Time'])

# Plotting the temperature data
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Temperature_C'], marker='o', label='Temperature (°C)')

# Set x-axis major locator to 30-second intervals
locator = mdates.SecondLocator(interval=30)  # Locator for every 30 seconds
plt.gca().xaxis.set_major_locator(locator)

# Custom formatter to remove the first digit of the minute
def custom_formatter(x, pos):
    label = mdates.DateFormatter('%M:%S')(x)
    if label.startswith('0'):
        return label[1:]  # Remove the first character if it's '0'
    return label[1:]  # Otherwise, return the last two characters (the last minute digit and seconds)

plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(custom_formatter))

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

plt.title('Temperature Over Time')
plt.xlabel('Time (minute:seconds)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()  # Adjust layout to make room for date labels
plt.show()
