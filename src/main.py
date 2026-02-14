import argparse
import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import load_csv
from src.analysis import perform_linear_fit, perform_polynomial_fit, perform_linear_fit_manual, evaluate_fit

#--------------------------------------------------------------------------------------
# Program workflow:
# 1. Load dataset from CSV
# 2. Choose regression model (linear or polynomial)
# 3. Compute model parameters
# 4. Evaluate model performance
# 5. Visualize results
#---------------------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Scientific Data Analyzer")

    parser.add_argument("--file", required=True)
    parser.add_argument("--model", choices=["linear", "polynomial"], default="linear")
    parser.add_argument("--degree", type=int, default=2)
    parser.add_argument("--method", choices=["manual", "numpy"], default="numpy")

    args = parser.parse_args()

    # Load data
    x, y = load_csv(args.file)

    # Plot raw data
    plt.scatter(x, y, label="Data")

    # ===============================
    # MODEL SELECTION
    # ===============================
    if args.model == "linear":

        if args.method == "manual":
            result = perform_linear_fit_manual(x, y)
        else:
            result = perform_linear_fit(x, y)

        y_fit = result["slope"] * x + result["intercept"]
        plt.plot(x, y_fit, label=f"Linear fit ({args.method})")
        
        # Evaluate how well the fitted model matches the observed data.
        # We compute regression performance metrics:
        # - MSE (Mean Squared Error): average squared difference between predicted and true values
        # - R² (Coefficient of Determination): proportion of variance explained by the model

        metrics = evaluate_fit(y, y_fit)
        print("\nModel performance:")
        print(f"MSE: {metrics['mse']:.4f}")
        print(f"R² : {metrics['r2']:.4f}")


    else:
        coeffs = perform_polynomial_fit(x, y, degree=args.degree)

        x_smooth = np.linspace(min(x), max(x), 300)
        y_smooth = np.polyval(coeffs, x_smooth)

        plt.plot(x_smooth, y_smooth, label=f"Polynomial fit (degree {args.degree})")

        # Evaluate the polynomial regression model by comparing predicted values (computed from polynomial coefficients)
        #  with the original observed data using MSE and R² metrics.

        metrics = evaluate_fit(y, np.polyval(coeffs, x))
        print("\nModel performance:")
        print(f"MSE: {metrics['mse']:.4f}")
        print(f"R2: {metrics['r2']:.4f}")


    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

