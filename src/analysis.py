import numpy as np

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