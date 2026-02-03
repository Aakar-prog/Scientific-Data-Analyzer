import os
import numpy as np
import pandas as pd

from src.data_loader import load_csv


def test_load_csv_success():
    test_file = "test_data.csv"

    # create test CSV with header
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    df.to_csv(test_file, index=False)

    x, y = load_csv(test_file)

    assert isinstance(x, np.ndarray)
    assert isinstance(y, np.ndarray)
    assert len(x) == 2
    assert len(y) == 2

    os.remove(test_file)


def test_file_not_found():
    try:
        load_csv("non_existent_file.csv")
        assert False
    except FileNotFoundError:
        assert True

