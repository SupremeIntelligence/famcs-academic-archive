import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

print ("Задание 1: Аппроксимация функции многочленами Лежандра","\n")
def x(t: float) -> float:
    "Исходная функция"
    return 2 * np.abs(t) - t 

def P0(t): return 1
def P1(t:float) -> float: return t
def P2(t:float) -> float: return (3*t**2 - 1)/2
def P3(t:float) -> float: return (5*t**3 - 3*t)/2

Pk = [P0, P1, P2, P3]

# Вычисление коэффициентов Фурье
def fourier_coefficient(k: int) -> float:
    #подынтегральное выражение
    integrand = lambda t: x(t) * Pk[k](t)
    #вычисление интеграла
    integral, _ = quad(integrand, -1, 1)
    return (2*k + 1)/2 * integral

C = [fourier_coefficient(k) for k in range(4)]
print(f"Коэффициенты фурье: {C}", "\n")

A0 = C[0] - 0.5 * C[2]
A1 = C[1] - 1.5 * C[3]
A2 = 1.5 * C[2]
A3 = 2.5 * C[3]

Ak = [A0, A1, A2, A3]

print("Аналитическое разложение аппроксимации в степенной форме:")
print(f"S(t) = {Ak[0]:.4f} + {Ak[1]:.4f}*t + {Ak[2]:.4f}*t^2 + {Ak[3]:.4f}*t^3")

def S(t:float) -> float:
    "Апроксимирующая функция"
    return Ak[0] + Ak[1]*t + Ak[2]*t**2 + Ak[3]*t**3

#Погрешность
error_integrand = lambda t: (x(t) - S(t))**2
error, _ = quad(error_integrand, -1, 1)
print(f"Среднеквадратичная погрешность: {error:.4f}")

#Построение графика
t_values = np.linspace(-1, 1, 200)
x_values = x(t_values)  
s_values = S(t_values)
plt.figure(figsize=(10, 5))
plt.plot(t_values, x_values, label="x(t) = 2|t| - t", color="blue")
plt.plot(t_values,
         s_values, 
         label=f"S(t) = {Ak[0]:.4f} + {Ak[1]:.4f}*t + {Ak[2]:.4f}*t^2 + {Ak[3]:.4f}*t^3",
         color="red")
plt.title("Аппроксимация функции многочленами Лежандра")
plt.xlabel("t")
plt.ylabel("Значение")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



