import pandas as pd
import os

def load_csv(filepath):
    """
    Loads a CSV file into a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded data.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file '{filepath}' was not found.")
    
    try:
        data = pd.read_csv(filepath)
        if data.empty:
            raise ValueError("The file is empty.")
        return data
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty or corrupted.")