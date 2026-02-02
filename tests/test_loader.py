import unittest
from src.data_loader import load_csv

class TestDataLoader(unittest.TestCase):
    
    def test_load_runs(self):
        # A simple test to check if the function exists
        result = load_csv("dummy.csv")
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()