import csv
import numpy as np
import pandas as pd

def load_csv(filepath):
    x = []
    y = []

    with open(filepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))

    return np.array(x), np.array(y)
