from data_loader import load_csv
from analysis import perform_linear_fit
import matplotlib.pyplot as plt

x, y = load_csv("example.csv")

result = perform_linear_fit(x, y)

print("Slope:", result["slope"])
print("Intercept:", result["intercept"])

plt.scatter(x, y)
plt.plot(x, result["slope"] * x + result["intercept"])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scientific Data Analyzer")
plt.show()
