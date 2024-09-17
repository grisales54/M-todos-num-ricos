import numpy as np
from scipy.integrate import odeint  #  Equivalente de ode45 python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Graficas 3D


def lorenz(x, t, beta):
    x1, x2, x3 = x
    dx1 = 10 * (x2 - x1)
    dx2 = x1 * (beta - x3) - x2
    dx3 = x1 * x2 - 8 / 3 * x3
    return [dx1, dx2, dx3]


t = np.linspace(0, 100, 10000)  # tiempo de 0 a 100 segundos
x0 = [1, 1, 1]  # condiciones iniciales

# Para β = 1
beta1 = 1
sol1 = odeint(lorenz, x0, t, args=(beta1,))


# Gráficas para β = 1
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

ax1.plot(t, sol1[:, 0], "b", label="x₁")
ax1.set_xlabel("t")
ax1.set_ylabel("x₁")
ax1.legend()

ax2.plot(t, sol1[:, 1], "r", label="x₂")
ax2.set_xlabel("t")
ax2.set_ylabel("x₂")
ax2.legend()

ax3.plot(t, sol1[:, 2], "g", label="x₃")
ax3.set_xlabel("t")
ax3.set_ylabel("x₃")
ax3.legend()

plt.tight_layout()
plt.title("Sistema de Lorenz: β = 1")
plt.show()

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")
ax.plot(sol1[:, 0], sol1[:, 1], sol1[:, 2])
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("x3")
plt.title("Atractor de Lorenz: β = 1")
plt.show()

# Para β = 28
beta2 = 28
sol2 = odeint(lorenz, x0, t, args=(beta2,))

# Gráficas para β = 28
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

ax1.plot(t, sol2[:, 0], "b", label="x1")
ax1.set_xlabel("t")
ax1.set_ylabel("x1")
ax1.legend()

ax2.plot(t, sol2[:, 1], "r", label="x2")
ax2.set_xlabel("t")
ax2.set_ylabel("x2")
ax2.legend()

ax3.plot(t, sol2[:, 2], "g", label="x3")
ax3.set_xlabel("t")
ax3.set_ylabel("x3")
ax3.legend()

plt.tight_layout()
plt.title("Sistema de Lorenz: β = 28")
plt.show()

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")
ax.plot(sol2[:, 0], sol2[:, 1], sol2[:, 2])
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("x2")
plt.title("Atractor de Lorenz: β = 28")
plt.show()
