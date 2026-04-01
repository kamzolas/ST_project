# 🚀 test_script.py - interactive and exploratory example

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 1️⃣ Print current working directory
print("Current working directory:", os.getcwd())

# 2️⃣ Generate some synthetic data
x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 3️⃣ Create a DataFrame (like a table in R)
df = pd.DataFrame({"x": x, "sin": y_sin, "cos": y_cos})

print("\nFirst 5 rows of our data table:")
print(df.head())

# 4️⃣ Plot multiple lines
plt.figure(figsize=(8, 5))
plt.plot(df["x"], df["sin"], label="sin(x)", color="blue")
plt.plot(df["x"], df["cos"], label="cos(x)", color="red")
plt.title("Sine & Cosine Waves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# 5️⃣ Save the figure (essential on HPC)
plt.savefig("sine_cos_plot.png", dpi=150)
print("\nPlot saved as sine_cos_plot.png")

# 6️⃣ Interactive (if using VS Code Interactive Window)
plt.show()

# 7️⃣ Simple calculation: mean values
mean_sin = df["sin"].mean()
mean_cos = df["cos"].mean()
print(f"\nMean of sin(x): {mean_sin:.3f}, Mean of cos(x): {mean_cos:.3f}")
