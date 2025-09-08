import csv
import random

# Parameters for the linear relationship: y = mx + b + noise
m = 2.5   # slope
b = 10    # intercept
noise_level = 5  # maximum random noise

filename = "linear_regression_data.csv"
num_points = 3000

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["x", "y"])  # header

    for _ in range(num_points):
        x = random.uniform(0, 100)  # x values between 0 and 100
        noise = random.uniform(-noise_level, noise_level)
        y = m * x + b + noise
        writer.writerow([x, y])

print(f"{num_points} data points saved to {filename}")