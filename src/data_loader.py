
import numpy as np
import csv

def load_csv(filepath):
    x = []
    y = []

    with open(filepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                x.append(float(row[0]))
                y.append(float(row[1]))
            except ValueError:
                continue

    return np.array(x), np.array(y)
