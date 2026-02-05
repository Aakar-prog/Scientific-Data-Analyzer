import numpy as np
import matplotlib.pyplot as plt
from typing import Dict
from src.analysis import perform_linear_fit, perform_polynomial_fit




def calculate_basic_stats(data: np.ndarray) -> Dict[str, float]:

    """
    Calculates mean and standard deviation of a dataset.
    
    Args:
        data (array-like): A list or array of numerical data.
        
    Returns:
        dict: A dictionary containing 'mean' and 'std_dev'.
    """
    if len(data) == 0:
        return None
        
    return {
        "mean": np.mean(data),
        "std_dev": np.std(data)
    }
def perform_linear_fit(x_data: np.ndarray, y_data: np.ndarray) -> Dict[str, float]:

    """
    Performs a linear regression (y = mx + q).
    
    Args:
        x_data (array-like): Independent variable.
        y_data (array-like): Dependent variable.
        
    Returns:
        dict: Slope (m) and Intercept (q).
    """
    if len(x_data) != len(y_data) or len(x_data) == 0:
        return None
        
    # Fit a polynomial of degree 1 (Linear)
    slope, intercept = np.polyfit(x_data, y_data, 1)
    
    return {
        "slope": slope,
        "intercept": intercept
    }
def perform_polynomial_fit(
    x_data: np.ndarray,
    y_data: np.ndarray,
    degree: int = 2
) -> np.ndarray:
    """
    Perform polynomial regression of given degree.

    Parameters
    ----------
    x_data : np.ndarray
        Independent variable.
    y_data : np.ndarray
        Dependent variable.
    degree : int
        Degree of the polynomial.

    Returns
    -------
    np.ndarray
        Polynomial coefficients (highest power first).
    """
    if degree < 1:
        raise ValueError("Polynomial degree must be >= 1")

    return np.polyfit(x_data, y_data, degree)

# Plotting the graph

def plot_data(x, y):
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scientific Data Plot")
    plt.show()


