import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100)
dt = t[1] - t[0]

# начальное приближение
x = np.zeros_like(t)

for _ in range(2000):
    x_new = 2*t + 2 - np.cumsum(x)*dt
    x = x_new

plt.plot(t, x)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("Решение Вольтерра методом последовательных приближений")
plt.show()
