import unittest
import numpy as np
from src.analysis import perform_linear_fit, perform_polynomial_fit

#-----------------------------------------------------------------------
# Unit tests for regression analysis functions.
# These tests verify correctness of parameter estimation
# and expected output structure.
#............................................................................

class TestAnalysis(unittest.TestCase):

    # Verify linear regression recovers exact parameters
    # for a perfectly linear dataset: y = 2x + 1


    def test_linear_fit(self):
        x = [1, 2, 3]
        y = [3, 5, 7]

        result = perform_linear_fit(x, y)

        self.assertAlmostEqual(result["slope"], 2.0, places=5)
        self.assertAlmostEqual(result["intercept"], 1.0, places=5)

    def test_polynomial_fit(self):
        """
        Check that polynomial regression identifies correct model degree
        and returns expected number of coefficients.
        
        """

        x = np.array([0, 1, 2, 3])
        y = np.array([0, 1, 4, 9])

        coeffs = perform_polynomial_fit(x, y, degree=2)

        # Quadratic polynomial → 3 coefficients
        self.assertEqual(len(coeffs), 3)


if __name__ == "__main__":
    unittest.main()
