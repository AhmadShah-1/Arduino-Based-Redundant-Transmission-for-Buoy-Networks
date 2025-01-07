import pandas as pd
import matplotlib.pyplot as plt

# Path to your Excel file (update if needed)
file_path = 'sensor_data7cm_4hz_third.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Check that the required columns are present
if 'Elapsed Time (s)' in df.columns and 'Power (W)' in df.columns:
    # Plot Power vs. Elapsed Time
    plt.figure(figsize=(10, 6))
    plt.plot(df['Elapsed Time (s)'], df['Power (W)'], color='purple', label='Power')
    plt.xlabel('Elapsed Time (s)')
    plt.ylabel('Power (W)')
    plt.title('Power Over Time')
    plt.legend()
    plt.grid(True)

    # Display the plot
    plt.show()
else:
    print("The required columns ('Elapsed Time (s)', 'Power (W)') are not present in the Excel file. Please check the column names.")
