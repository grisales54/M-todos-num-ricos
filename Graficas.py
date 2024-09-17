import numpy as np
import matplotlib.pyplot as plt
import math as m


def f(x):
    y = (
        1
        + (2 * x)
        - (3 * x**2) * np.exp(-x)
        + (2 * x**3) * (np.sin(x)) * np.exp(-x / 5)
    )
    return y


x = np.linspace(4, 20, 1000)
y = f(x)


plt.plot(x, y, label="f(x)")
plt.grid(True)
plt.axhline(0, 0, color="black")
plt.axvline(0, 0, color="black")
plt.show()
