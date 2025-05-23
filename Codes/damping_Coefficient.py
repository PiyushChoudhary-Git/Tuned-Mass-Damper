import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

df = pd.read_csv("test1.csv")

df["Time (s)"] = df["Time"] / 1000.0

time = df["Time"].values
acc = df["Acceleration"].values

peaks, _ = find_peaks(acc, distance=1)  


plt.plot(time, acc, label="Acceleration")
plt.plot(time[peaks], acc[peaks], "ro", label="Peaks")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.title("Acceleration Peaks")
plt.legend()
plt.grid(True)
plt.show()


if len(peaks) >= 15:
    p1=1
    p2=14
    x1 = acc[peaks[p1]]
    x2 = acc[peaks[p2]]
    delta = np.log(abs(x1 / x2))/(p2-p1)
    zeta = delta / np.sqrt((2 * np.pi)**2 + delta**2)

    print(f"Peak 1 Amplitude: {x1:.4f}")
    print(f"Peak 2 Amplitude: {x2:.4f}")
    print(f"Logarithmic Decrement (δ): {delta:.4f}")
    print(f"Damping Ratio (ζ): {zeta:.4f}")

else:
    print("Not enough peaks to compute damping.")
