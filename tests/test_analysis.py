import unittest
from src.analysis import calculate_basic_stats, perform_linear_fit, perform_polynomial_fit

class TestAnalysis(unittest.TestCase):
    
    def test_calculate_stats(self):
        # Test mean and std dev
        data = [1, 2, 3]
        stats = calculate_basic_stats(data)
        
        self.assertEqual(stats['mean'], 2.0)
        self.assertAlmostEqual(stats['std_dev'], 0.81649658, places=5)

    def test_empty_data(self):
        # Test empty input safety
        result = calculate_basic_stats([])
        self.assertIsNone(result)

    def test_linear_fit(self):
        # Test linear regression (y = 2x + 1)
        x = [1, 2, 3]
        y = [3, 5, 7] 
        
        result = perform_linear_fit(x, y)
        
        # Check slope (m=2) and intercept (q=1)
        self.assertAlmostEqual(result['slope'], 2.0, places=5)
        self.assertAlmostEqual(result['intercept'], 1.0, places=5)

if __name__ == '__main__':
    unittest.main()

    def test_polynomial_fit_quadratic():
    """
    Test polynomial fitting for a simple quadratic function y = x^2
    """
    x = np.array([0, 1, 2, 3])
    y = np.array([0, 1, 4, 9])

    coeffs = perform_polynomial_fit(x, y, degree=2)

    # A quadratic polynomial must have 3 coefficients
    assert len(coeffs) == 3
