import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel file (update if needed)
file_path = 'sensor_data7cm_4hz_third.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Check that all the expected columns are present
required_columns = [
    'Elapsed Time (s)',
    'Temp (°C)',
    'Voltage (V)',
    'Current (mA)',
    'Power (W)'
]

# Ensure the required columns are in the DataFrame
if all(col in df.columns for col in required_columns):
    # Create a figure and four subplots (2 rows, 2 columns)
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # 1) Temperature vs. Elapsed Time (top-left)
    axs[0, 0].plot(df['Elapsed Time (s)'], df['Temp (°C)'], color='red', label='Temperature')
    axs[0, 0].set_xlabel('Elapsed Time (s)')
    axs[0, 0].set_ylabel('Temperature (°C)')
    axs[0, 0].set_title('Temperature Over Time')
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    # 2) Voltage vs. Elapsed Time (top-right)
    axs[0, 1].plot(df['Elapsed Time (s)'], df['Voltage (V)'], color='blue', label='Voltage')
    axs[0, 1].set_xlabel('Elapsed Time (s)')
    axs[0, 1].set_ylabel('Voltage (V)')
    axs[0, 1].set_title('Voltage Over Time')
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # 3) Current vs. Elapsed Time (bottom-left)
    axs[1, 0].plot(df['Elapsed Time (s)'], df['Current (mA)'], color='green', label='Current')
    axs[1, 0].set_xlabel('Elapsed Time (s)')
    axs[1, 0].set_ylabel('Current (mA)')
    axs[1, 0].set_title('Current Over Time')
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    # 4) Power vs. Elapsed Time (bottom-right)
    axs[1, 1].plot(df['Elapsed Time (s)'], df['Power (W)'], color='purple', label='Power')
    axs[1, 1].set_xlabel('Elapsed Time (s)')
    axs[1, 1].set_ylabel('Power (W)')
    axs[1, 1].set_title('Power Over Time')
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    # Adjust spacing between subplots to prevent overlap
    plt.tight_layout()

    # Display the combined figure
    plt.show()

else:
    print("The required columns are not present in the Excel file. Please check the column names.")
