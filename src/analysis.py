import numpy as np
import matplotlib.pyplot as plt


def calculate_basic_stats(data):
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
def perform_linear_fit(x_data, y_data):
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

def plot_data(x, y):
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scientific Data Plot")
    plt.show()
