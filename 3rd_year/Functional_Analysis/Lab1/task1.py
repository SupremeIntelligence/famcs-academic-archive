import numpy as np
import matplotlib.pyplot as plt
import math

eps = 1e-4          # требуемая точность
x0 = 0.5            # начальное приближение
a, b = 0, 1          # границы отрезка поиска корня

def g(x: float) -> float:
    return x**7 + x**3 + 2*x**2 + x - 1

def f_n(x: float, lambda_: float) -> float:
    return x - lambda_ * g(x)

def g_derivative(x: float) -> float:
    return 7*x**6 + 3*x**2 + 4*x + 1

def aprior_estimate(eps: float,
                    alpha: float,
                    x1: float,
                    x0: float) -> int:
    n_aprior = math.ceil(math.log((eps * (1 - alpha)) / abs(x1 - x0), alpha)) + 1
    return n_aprior

g1 = g_derivative(a)
g2 = g_derivative(b)
lambda_ = 2/(g1 + g2)
alpha = (g2 - g1) / (g1 + g2)
x1 = f_n(x0,lambda_)

n_aprior = aprior_estimate(eps, abs(alpha), x1, x0)

print(f"Априорная оценка числа итераций: n = {n_aprior}")

n = 0
x_prev = x0
x_curr = f_n(x_prev, lambda_)

while abs(x_curr - x_prev) > eps:
    n += 1
    x_prev, x_curr = x_curr, f_n(x_curr, lambda_)

print("\nРезультаты итераций:")
print(f"Последняя итерация n = {n}")
print(f"x* ≈ {x_curr:.8f}")
print(f"|g(x*)| = {abs(g(x_curr)):.8e}")

xs = np.linspace(a, b, 200)
ys = g(xs)

plt.figure(figsize=(8, 5))
plt.plot(xs, ys, label='g(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.8)
plt.title("График g(x) = 0")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.legend()
plt.grid(True)
plt.show()