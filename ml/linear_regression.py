import csv

input_file = "linear_regression_data.csv"
summary_file = "process_summary.txt"

total_ratio = 0
count = 0

with open(input_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x = float(row['x'])
        y = float(row['y'])
        if x != 0:  # avoid division by zero
            total_ratio += y / x
            count += 1

average_ratio = total_ratio / count if count != 0 else 0

# Write summary to a file
with open(summary_file, mode='w') as f:
    f.write("Linear Regression Data Analysis Summary\n")
    f.write("--------------------------------------\n")
    f.write(f"Input file: {input_file}\n")
    f.write(f"Total data points processed: {count}\n")
    f.write(f"Average ratio (y/x): {average_ratio:.4f}\n")
    f.write("\nNotes:\n")
    f.write("- Points with x=0 were ignored to avoid division errors.\n")
    f.write("- This average ratio can be used as a rough predictor but may not be as accurate as proper linear regression.\n")

print(f"Process summary written to {summary_file}")