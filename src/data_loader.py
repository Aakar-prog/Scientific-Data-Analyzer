import csv
import numpy as np

def load_csv(filepath):
    x = []
    y = []

    with open(filepath, "r", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            # skip empty or malformed rows
            if not row or len(row) < 2:
                continue

            x.append(float(row[0].strip()))
            y.append(float(row[1].strip()))

    return np.array(x), np.array(y)

