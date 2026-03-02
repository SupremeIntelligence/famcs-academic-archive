import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

print ("Задание 3: Аппроксимация функции тригонометрическим многочленом","\n")
def x(t):
    return 2*t - t**2

a, b = -np.pi, np.pi
xs = np.linspace(a, b, 20001)
ys = x(xs)

def fourier_coefficients(func, N_max):
    """Вычисление коэффициентов Фурье"""
    a0 = quad(func, a, b)[0] / np.pi
    
    a_coeffs = np.zeros(N_max)
    b_coeffs = np.zeros(N_max)
    
    for n in range(1, N_max + 1):
        a_coeffs[n-1] = quad(lambda t: func(t) * np.cos(n*t), a, b)[0] / np.pi
        b_coeffs[n-1] = quad(lambda t: func(t) * np.sin(n*t), a, b)[0] / np.pi
    
    return a0, a_coeffs, b_coeffs

print (a)
print(b)

def trig_polynom(t, a0, a_coeffs, b_coeffs, N):
    """Тригонометрический многочлен степени N"""
    result = a0 / 2
    for n in range(1, N + 1):
        result += a_coeffs[n-1] * np.cos(n*t) + b_coeffs[n-1] * np.sin(n*t)
    return result

#Ищем минимальную степень для точности epsilon = 1e-3
epsilon = 1e-3
N_max = 10
a0, a_coeffs, b_coeffs = fourier_coefficients(x, N_max)

#Находим достаточную степень
N_sufficient = 1
for N in range(1, N_max + 1):
    p = np.array([trig_polynom(t, a0, a_coeffs, b_coeffs, N) for t in xs])
    L2_err = np.sqrt(np.trapezoid((ys - p)**2, xs))
    if L2_err < epsilon:
        N_sufficient = N
        break

#Финальное приближение
p_final = np.array([trig_polynom(t, a0, a_coeffs, b_coeffs, N_sufficient) for t in xs])

#Погрешность
L2_err = np.sqrt(np.trapezoid((ys - p_final)**2, xs))
max_err = np.max(np.abs(ys - p_final))

print("Тригонометрический многочлен:")
print(f"p(t) = {a0/2:.6f}")

for n in range(1, N_sufficient + 1):
    a_n = a_coeffs[n-1]
    b_n = b_coeffs[n-1]
    if abs(a_n) > 1e-3:
        print(f"{a_n:+.6f} * cos({n}t)")
    if abs(b_n) > 1e-3:
        print(f"{b_n:+.6f} * sin({n}t)")

print(f"\nСтепень тригонометрического многочлена: N = {N_sufficient}")
print(f"L2 ошибка ≈ {L2_err:.6g}")
print(f"ошибка ≈ {max_err:.6g}")

#График
plt.figure(figsize=(10, 6))
plt.plot(xs, ys, label='x(t) = 2t - t²', linewidth=2)
plt.plot(xs, p_final, '--', label=f'Тригонометрический многочлен (N={N_sufficient})', linewidth=2)
plt.title('Аппроксимация функции x(t) тригонометрическим многочленом')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()