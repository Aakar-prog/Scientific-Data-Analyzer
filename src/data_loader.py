import csv
import numpy as np

def load_csv(filepath):
    x = []
    y = []

    with open(filepath, "r", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            if not row or len(row) < 2:
                continue

            try:
                x.append(float(row[0].strip()))
                y.append(float(row[1].strip()))
            except ValueError:
                # Skip header or non-numeric rows
                continue

    return np.array(x), np.array(y)


