import pandas as pd

def process_data(file_path):
    data = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('['):
                continue

            parts = line.strip().split(', ')
            time = parts[0].split(':')[1]
            temperature = parts[1].split(': ')[1]
            turbidity = parts[2].split(': ')[1]

            data.append({'Time': time, 'Temperature': temperature, 'Turbidity': turbidity})

    return data

# Process the data
file_path = 'temp.txt'  # Replace with your actual file path
data = process_data(file_path)

# Convert to DataFrame and save as Excel
df = pd.DataFrame(data)
excel_path = 'processed_data.xlsx'  # Replace with your desired excel file path
df.to_excel(excel_path, index=False)

print(f"Data saved to {excel_path}")
