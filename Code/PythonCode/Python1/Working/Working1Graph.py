import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file (make sure the file path and name are correct)
file_path = 'sensor_data7cm_4hz_third.xlsx'  # Change if needed
df = pd.read_excel(file_path)

# Define the columns you expect to see in your DataFrame
required_columns = ['Elapsed Time', 'Temp', 'Voltage', 'Current']

# Check if all the required columns are present
if all(col in df.columns for col in required_columns):
    # Create a figure with three subplots, one for each measurement
    plt.figure(figsize=(10, 8))

    # 1) Temperature vs. Elapsed Time
    plt.subplot(3, 1, 1)
    plt.plot(df['Elapsed Time'], df['Temp'], color='red', label='Temperature')
    plt.xlabel('Elapsed Time (seconds)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Over Time')
    plt.legend()
    plt.grid(True)

    # 2) Voltage vs. Elapsed Time
    plt.subplot(3, 1, 2)
    plt.plot(df['Elapsed Time'], df['Voltage'], color='blue', label='Voltage')
    plt.xlabel('Elapsed Time (seconds)')
    plt.ylabel('Voltage (V)')
    plt.title('Voltage Over Time')
    plt.legend()
    plt.grid(True)

    # 3) Current vs. Elapsed Time
    plt.subplot(3, 1, 3)
    plt.plot(df['Elapsed Time'], df['Current'], color='green', label='Current')
    plt.xlabel('Elapsed Time (seconds)')
    plt.ylabel('Current (mA)')
    plt.title('Current Over Time')
    plt.legend()
    plt.grid(True)

    # Adjust layout to prevent overlapping text
    plt.tight_layout()

    # Display the plots
    plt.show()
else:
    print("The required columns (Elapsed Time, Temp, Voltage, Current) are not present in the Excel file. Please check the column names.")
