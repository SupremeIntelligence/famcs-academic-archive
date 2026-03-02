import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

print ("Задание 2: Аппроксимация функции многочленами Чебышева первого рода","\n")

#Исходная функция
def x(t):
    return t * np.sin(0.5 * t)**2

#Многочлены Чебышева первого рода
def T(k, t):
    return np.cos(k * np.arccos(t))

#Коэфициенты
def cheb_coeff(k):
    if k == 0:
        c, _ = quad(lambda t: x(t) / np.sqrt(1 - t**2), -1, 1)
        return c / np.pi
    else:
        c, _ = quad(lambda t: x(t) * T(k, t) / np.sqrt(1 - t**2), -1, 1)
        return 2 * c / np.pi

#Степень аппроксимирующего многочлена
n = 5
C = [cheb_coeff(k) for k in range(n + 1)]

print("Коэффициенты Чебышева C_k:")
for k, ck in enumerate(C):
    print(f"C_{k} = {ck:.10f}")

#Построение аппроксимации
t_vals = np.linspace(-1, 1, 400)
S_vals = sum(C[k] * T(k, t_vals) for k in range(n + 1))
x_vals = x(t_vals)

#Погрешности
L2_err = np.sqrt(np.trapezoid((x_vals - S_vals)**2, t_vals))
max_err = np.max(np.abs(x_vals - S_vals))
print(f"\nL2 ошибка ≈ {L2_err:.6g}")
print(f"ошибка ≈ {max_err:.6g}")

#График
plt.figure(figsize=(9,5))
plt.plot(t_vals, x_vals, label='x(t) = t·sin²(t/2)', linewidth=2)
plt.plot(t_vals, S_vals, '--', label='Аппроксимация Чебышева (степень ≤ 5)', linewidth=2)
plt.xlabel('t')
plt.ylabel('Значение')
plt.title('Аппроксимация функции x(t) многочленами Чебышева I рода')
plt.grid(True)
plt.legend()
plt.show()