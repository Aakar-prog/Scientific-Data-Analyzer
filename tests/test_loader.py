import unittest
import pandas as pd
import os
from src.data_loader import load_csv

class TestDataLoader(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary dummy CSV file for testing
        self.test_file = "test_data.csv"
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        df.to_csv(self.test_file, index=False)
        
    def tearDown(self):
        # Clean up: delete the file after test finishes
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
    def test_load_csv_success(self):
        # Test if data loads correctly
        df = load_csv(self.test_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)  # We put 2 rows in, should get 2 out

    def test_file_not_found(self):
        # Test if it handles missing files correctly
        with self.assertRaises(FileNotFoundError):
            load_csv("non_existent_file.csv")

if __name__ == '__main__':
    unittest.main()