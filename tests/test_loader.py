import os
import unittest
import numpy as np
import pandas as pd

from src.data_loader import load_csv


class TestLoader(unittest.TestCase):
    """Tests for CSV loading functionality."""

    def test_load_csv_success(self):
        """CSV should load correctly and return numpy arrays."""

        test_file = "test_data.csv"

        # Create temporary CSV
        df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        df.to_csv(test_file, index=False)

        x, y = load_csv(test_file)

        self.assertIsInstance(x, np.ndarray)
        self.assertIsInstance(y, np.ndarray)
        self.assertEqual(len(x), 2)
        self.assertEqual(len(y), 2)

        os.remove(test_file)

    def test_file_not_found(self):
        """Invalid path should raise FileNotFoundError."""

        with self.assertRaises(FileNotFoundError):
            load_csv("non_existent_file.csv")


if __name__ == "__main__":
    unittest.main()



