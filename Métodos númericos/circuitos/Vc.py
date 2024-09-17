import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = 12 - (12) * np.exp(-x / 18.04)
    return y


x = np.linspace(0, 150)

y = f(x)


plt.plot(x, y, label="f(x)")
plt.grid(True)
plt.axhline(0, 0, color="black")
plt.axvline(0, 0, color="black")
plt.show()
