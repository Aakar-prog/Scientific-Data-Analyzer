import numpy as np
import matplotlib.pyplot as plt
from typing import Dict

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
    # Perform polynomial regression of given degree.

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

#----------------------------------------------------------------------------
# Manual linear regression using the Normal Equation:
# θ = (XᵀX)^(-1) Xᵀ y
# This implementation estimates slope and intercept without using NumPy's
# high-level fitting routines, allowing comparison with np.polyfit().
#------------------------------------------------------------------------------

def perform_linear_fit_manual(x: np.ndarray, y: np.ndarray) -> dict:
    """
    Linear regression using the normal equation:
        theta = (X^T X)^(-1) X^T y
    """

    # Convert to column vectors
    x = np.asarray(x)
    y = np.asarray(y)

    # Design matrix [1, x]
    X = np.column_stack((np.ones(len(x)), x))

    # Normal equation
    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    intercept = theta[0]
    slope = theta[1]

    return {"slope": slope, "intercept": intercept}


# Plotting the graph

def plot_data(x, y):
    plt.scatter(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scientific Data Plot")
    plt.show()

# -------------------------------------------------------
# Model evaluation metrics
# Computes prediction error and goodness of fit
# -------------------------------------------------------


def evaluate_fit(y_true, y_pred):
    """
    Compute error metrics for model evaluation.
    Returns Mean Squared Error (MSE) and R² score.
    """
    mse = np.mean((y_true - y_pred) ** 2)
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_pred) ** 2)
    r2 = 1 - (ss_residual / ss_total)

    return {"mse": mse, "r2": r2}



