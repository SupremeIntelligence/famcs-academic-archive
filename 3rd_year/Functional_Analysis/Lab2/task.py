import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def x(t):
    return 2 * np.abs(t) - t 

# Полиномы Лежандра
def P0(t): return 1
def P1(t): return t
def P2(t): return (3*t**2 - 1)/2
def P3(t): return (5*t**3 - 3*t)/2

Pk = [P0, P1, P2, P3]

# Вычисление коэффициентов Фурье
def fourier_coeff(k):
    integrand = lambda t: x(t) * Pk[k](t)
    integral, _ = quad(integrand, -1, 1)
    return (2*k + 1)/2 * integral

# Коэффициенты Фурье
C = [fourier_coeff(k) for k in range(4)]
print(C)

# Преобразование в степенной вид:
# P0 = 1
# P1 = t
# P2 = (3/2)t^2 - 1/2
# P3 = (5/2)t^3 - (3/2)t

a0 = C[0] - 0.5 * C[2]
a1 = C[1] - 1.5 * C[3]
a2 = 1.5 * C[2]
a3 = 2.5 * C[3]

# Вывод разложения
print("Аналитическое разложение аппроксимации в степенной форме:")
print(f"S(t) = {a0:.4f} + {a1:.4f}*t + {a2:.4f}*t^2 + {a3:.4f}*t^3")

# Аппроксимирующая функция
def S(t):
    return a0 + a1*t + a2*t**2 + a3*t**3

# Точки для графика
t_vals = np.linspace(-1, 1, 400)
x_vals = 2 * np.abs(t_vals) - t_vals  # для массивов используем np.abs
S_vals = S(t_vals)

# График
plt.figure(figsize=(10, 5))
plt.plot(t_vals, x_vals, label='x(t) = 2|t| - t', color='blue')
plt.plot(t_vals, S_vals, label='Аппроксимация Лежандра (степенной вид)', color='red', linestyle='--')
plt.title('Аппроксимация функции многочленами Лежандра')
plt.xlabel('t')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Погрешность
error_integrand = lambda t: (x(t) - S(t))**2
error, _ = quad(error_integrand, -1, 1)
print(f"Среднеквадратичная погрешность: {error:.4f}")

#_________________________________

# === 1. Исходная функция ===
def x(t):
    """Функция из задания 2.1.6: x(t) = 0.5 * t * sin^2(t)"""
    return  t * np.sin(0.5 * t)**2

# === 2. Создаём плотную сетку для интегрирования и построения ===
xs = np.linspace(-1, 1, 20001)
ys = x(xs)

# === 3. Аппроксимация функцией - многочленом степени <= 5 ===
deg = 5
V = np.vander(xs, deg + 1)
coeffs = np.linalg.lstsq(V, ys, rcond=None)[0]
coeffs_rev = coeffs[::-1]
p = np.polyval(coeffs, xs)

# === 4. Считаем погрешности ===
L2_err = np.sqrt(np.trapezoid((ys - p)**2, xs))
max_err = np.max(np.abs(ys - p))

# === 5. Выводим результаты ===
print("Найденный многочлен степени <= 5 (коэффициенты от младшего к старшему):")
for i, a in enumerate(coeffs_rev):
    print(f"a_{i} = {a:.12g}")

print("\nПолином в виде:")
print("p(t) = " + " + ".join([f"{coeffs_rev[i]:+.6g} * t^{i}" for i in range(len(coeffs_rev))]))

print(f"\nL2 ошибка ≈ {L2_err:.6g}")
print(f"Максимальная абсолютная ошибка ≈ {max_err:.6g}")

# === 6. График ===
plt.figure(figsize=(8,5))
plt.plot(xs, ys, label='x(t) = 0.5 * t * sin^2(t)', linewidth=2)
plt.plot(xs, p, '--', label='Полином степени <= 5', linewidth=2)
plt.title('Аппроксимация функции x(t) многочленом степени <= 5')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

#__________________________________________
# === 1. Исходная функция ===
def x(t):
    """Функция из задания 3.6: x(t) = 2t - t^2"""
    return 2*t - t**2

# === 2. Создаём плотную сетку для интегрирования и построения ===
a, b = -np.pi, np.pi
xs = np.linspace(a, b, 20001)
ys = x(xs)

# === 3. Аппроксимация тригонометрическим многочленом ===
def compute_fourier_coeffs(func, N_max):
    """Вычисление коэффициентов Фурье"""
    a0 = quad(func, a, b)[0] / np.pi
    
    a_coeffs = np.zeros(N_max)
    b_coeffs = np.zeros(N_max)
    
    for n in range(1, N_max + 1):
        a_coeffs[n-1] = quad(lambda t: func(t) * np.cos(n*t), a, b)[0] / np.pi
        b_coeffs[n-1] = quad(lambda t: func(t) * np.sin(n*t), a, b)[0] / np.pi
    
    return a0, a_coeffs, b_coeffs

def trig_poly(t, a0, a_coeffs, b_coeffs, N):
    """Тригонометрический многочлен степени N"""
    result = a0 / 2
    for n in range(1, N + 1):
        result += a_coeffs[n-1] * np.cos(n*t) + b_coeffs[n-1] * np.sin(n*t)
    return result

# Ищем минимальную степень для точности epsilon = 1e-3
epsilon = 1e-3
N_max = 10
a0, a_coeffs, b_coeffs = compute_fourier_coeffs(x, N_max)

# Находим достаточную степень
N_sufficient = 1
for N in range(1, N_max + 1):
    p = np.array([trig_poly(t, a0, a_coeffs, b_coeffs, N) for t in xs])
    L2_err = np.sqrt(np.trapezoid((ys - p)**2, xs))
    if L2_err < epsilon:
        N_sufficient = N
        break

# Финальное приближение
p_final = np.array([trig_poly(t, a0, a_coeffs, b_coeffs, N_sufficient) for t in xs])

# === 4. Считаем погрешности ===
L2_err = np.sqrt(np.trapezoid((ys - p_final)**2, xs))
max_err = np.max(np.abs(ys - p_final))

# === 5. Выводим результаты ===
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
print(f"Максимальная абсолютная ошибка ≈ {max_err:.6g}")

# === 6. График ===
plt.figure(figsize=(10, 6))
plt.plot(xs, ys, label='x(t) = 2t - t²', linewidth=2)
plt.plot(xs, p_final, '--', label=f'Тригонометрический многочлен (N={N_sufficient})', linewidth=2)
plt.title('Аппроксимация функции x(t) тригонометрическим многочленом')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
#________________