from data_loader import load_csv
from analysis import perform_linear_fit
import matplotlib.pyplot as plt

x, y = load_csv("example.csv")

result = perform_linear_fit(x, y)

print("Slope:", result["slope"])
print("Intercept:", result["intercept"])

plt.scatter(x, y, label="Data")
plt.plot(
    x,
    result["slope"] * x + result["intercept"],
    label=f"Fit: y = {result['slope']:.2f}x + {result['intercept']:.2e}"
)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scientific Data Analyzer")
plt.legend()
plt.show()

