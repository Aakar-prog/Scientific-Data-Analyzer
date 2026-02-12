import argparse
import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import load_csv
from src.analysis import perform_linear_fit, perform_polynomial_fit

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

    # Model selection
    if args.model == "linear":
        if args.method == "manual":
            result = perform_linear_fit_manual(x, y)
        else:
            result = perform_linear_fit(x, y)

        y_fit = result["slope"] * x + result["intercept"]
        plt.plot(x, y_fit, label=f"Linear fit ({args.method})")

    else:
        coeffs = perform_polynomial_fit(x, y, degree=args.degree)
        x_smooth = np.linspace(min(x), max(x), 300)
        y_smooth = np.polyval(coeffs, x_smooth)
        plt.plot(x_smooth, y_smooth, label=f"Polynomial degree {args.degree}")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()



