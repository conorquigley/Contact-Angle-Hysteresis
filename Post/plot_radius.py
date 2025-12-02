import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Number of files
num_files = 199  # 000 to 067
y_values = []

for i in range(1, num_files):
    filename = f"output/data/data_{i:03d}.csv"  # zero-padded to 3 digits

    if not os.path.isfile(filename):
        print(f"Warning: {filename} not found, skipping")
        y_values.append(np.nan)
        continue

    df = pd.read_csv(filename, header=None)

    # second last row
    second_last_row = df.iloc[-3]

    # second last value in that row
    value = second_last_row.iloc[-4]

    # Remove quotes and convert to float if possible
    try:
        value = float(str(value).strip("'").strip('"'))
    except ValueError:
        print(f"Could not convert value in {filename}: {value}")
        value = np.nan

    y_values.append(value)

x_values = np.arange(num_files)

print(max(y_values))
plt.figure(figsize=(8,5))
plt.plot(y_values, marker='o')
plt.xlabel('Timestep')
plt.ylabel('Droplet radius')
plt.title('Radius Over Timesteps')
plt.grid(True)
plt.show()
