import argparse
import numpy as np
import matplotlib.pyplot as plt

from src.data_loader import load_csv
from src.analysis import perform_linear_fit, perform_polynomial_fit


def main():
    # ----------------------------
    # Argument parser
    # ----------------------------
    parser = argparse.ArgumentParser(description="Scientific Data Analyzer")

    parser.add_argument(
        "--file",
        required=True,
        help="Path to CSV file containing x,y data"
    )

    parser.add_argument(
        "--model",
        choices=["linear", "polynomial"],
        default="linear",
        help="Regression model to use"
    )

    parser.add_argument(
        "--degree",
        type=int,
        default=2,
        help="Degree of polynomial (used only for polynomial model)"
    )

    args = parser.parse_args()   # ✅ args defined ONCE, early

    # ----------------------------
    # Load data
    # ----------------------------
    x, y = load_csv(args.file)

    # ----------------------------
    # Plot raw data
    # ----------------------------
    plt.scatter(x, y, label="Data")

    # ----------------------------
    # Linear model
    # ----------------------------
    if args.model == "linear":
        result = perform_linear_fit(x, y)

        y_fit = result["slope"] * x + result["intercept"]
        label = f"Linear fit: y = {result['slope']:.2f}x + {result['intercept']:.2f}"

        plt.plot(x, y_fit, label=label)

    # ----------------------------
    # Polynomial model
    # ----------------------------
    else:
        coeffs = perform_polynomial_fit(x, y, degree=args.degree)

        # Smooth curve
        x_smooth = np.linspace(min(x), max(x), 300)
        y_smooth = np.polyval(coeffs, x_smooth)

        plt.plot(
            x_smooth,
            y_smooth,
            label=f"Polynomial fit (degree {args.degree})"
        )

    # ----------------------------
    # Final plot styling
    # ----------------------------
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scientific Data Analyzer")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
