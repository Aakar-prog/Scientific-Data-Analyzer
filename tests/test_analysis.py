import unittest
from src.analysis import calculate_basic_stats

class TestAnalysis(unittest.TestCase):
    
    def test_calculate_stats(self):
        # We test with simple numbers: 1, 2, 3
        # Mean should be 2.0
        # Std Dev (population) of [1,2,3] is 0.816...
        data = [1, 2, 3]
        stats = calculate_basic_stats(data)
        
        self.assertEqual(stats['mean'], 2.0)
        self.assertAlmostEqual(stats['std_dev'], 0.81649658, places=5)

    def test_empty_data(self):
        # Test if it handles empty lists safely
        result = calculate_basic_stats([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()