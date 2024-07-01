import pandas as pd

# Replace 'data.txt' with the path to your file
file_path = 'data.txt'

# Initialize lists to store the parsed data
timestamps = []
voltages = []

# Read the file and parse the data
with open(file_path, 'r') as file:
    for line in file:
        # Split the line into timestamp and voltage
        parts = line.strip().split(',')
        if len(parts) == 2:
            try:
                # Convert timestamp from milliseconds to minutes
                timestamp = int(parts[0]) / 60000
                voltage = float(parts[1])
                timestamps.append(timestamp)
                voltages.append(voltage)
            except ValueError:
                # Handle the case where conversion fails
                print(f"Could not convert line: {line}")

# Create a DataFrame
df = pd.DataFrame({'Time (Minutes)': timestamps, 'Voltage': voltages})

# Write to an Excel file
excel_path = 'output.xlsx'
df.to_excel(excel_path, index=False, float_format="%.2f")

print(f"Data written to {excel_path}")
