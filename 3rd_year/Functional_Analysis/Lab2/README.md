# FAMCS Functional Analysis & Integral Equations Lab2

## English Version

**Topic:** Orthogonal and Least Squares Approximation of Functions

Implementation of numerical methods for polynomial and trigonometric approximation of functions.

---

### Task 1 — Legendre Polynomial Approximation

Approximate the function

$$
x(t) = 2|t| - t, \quad t \in [-1,1]
$$

using Legendre polynomials.

### Method

The Fourier–Legendre coefficients were computed as:

$$
C_k = \frac{2k+1}{2}\int_{-1}^{1} x(t) P_k(t)\,dt
$$

The approximation was constructed using polynomials up to degree 3 and transformed into power form.

The mean-square error was computed:

$$
\|x - S\|_{L^2}^2 = \int_{-1}^{1} (x(t) - S(t))^2 dt
$$

**Result:** Polynomial approximation obtained and visualized.

---

### Task 2 — Best Polynomial Approximation (Degree ≤ 5)

Approximate the function

$$
x(t) = t \sin^2\left(\frac{t}{2}\right), \quad t \in [-1,1]
$$

### Method

- Dense grid construction
- Vandermonde matrix
- Least squares solution
- Polynomial of degree ≤ 5

Errors computed:

$$
L^2 = \left( \int_{-1}^{1} (x(t) - p(t))^2 dt \right)^{1/2}
$$

and

$$
\|x - p\|_{\infty}
$$

**Result:** Best polynomial approximation found.

---

### Task 3 — Trigonometric Approximation (Fourier Series)

Approximate

$$
x(t) = 2t - t^2, \quad t \in [-\pi,\pi]
$$

### Method

Fourier coefficients:

$$
a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} x(t)\,dt
$$

$$
a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x(t)\cos(nt)\,dt
$$

$$
b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x(t)\sin(nt)\,dt
$$

Trigonometric polynomial:

$$
S_N(t) = \frac{a_0}{2} + \sum_{n=1}^{N} \left(a_n \cos nt + b_n \sin nt\right)
$$

The minimal degree \(N\) was selected such that

$$
\|x - S_N\|_{L^2} < \varepsilon
$$

**Result:** Trigonometric approximation constructed with required accuracy.

---

## Русская версия

**Тема:** Ортогональная и среднеквадратичная аппроксимация функций

Реализация численных методов полиномиальной и тригонометрической аппроксимации функций.

---

### Задание 1 — Аппроксимация многочленами Лежандра

Аппроксимировать функцию

$$
x(t) = 2|t| - t, \quad t \in [-1,1]
$$

### Метод

Коэффициенты Фурье–Лежандра вычислялись по формуле:

$$
C_k = \frac{2k+1}{2}\int_{-1}^{1} x(t) P_k(t)\,dt
$$

Аппроксимация построена с использованием многочленов до степени 3 и приведена к степенному виду.

Среднеквадратичная погрешность вычислялась как:

$$
\|x - S\|_{L^2}^2 = \int_{-1}^{1} (x(t) - S(t))^2 dt
$$

**Результат:** Получена и визуализирована полиномиальная аппроксимация.

---

### Задание 2 — Наилучшая полиномиальная аппроксимация (степень ≤ 5)

Аппроксимировать функцию

$$
x(t) = t \sin^2\left(\frac{t}{2}\right), \quad t \in [-1,1]
$$

### Метод

- Построение плотной сетки
- Формирование матрицы Вандермонда
- Решение задачи методом наименьших квадратов
- Построение многочлена степени ≤ 5

Вычислены погрешности:

$$
L^2 = \left( \int_{-1}^{1} (x(t) - p(t))^2 dt \right)^{1/2}
$$

и

$$
\|x - p\|_{\infty}
$$

**Результат:** Найдена наилучшая полиномиальная аппроксимация.

---

### Задание 3 — Тригонометрическая аппроксимация (ряд Фурье)

Аппроксимировать функцию

$$
x(t) = 2t - t^2, \quad t \in [-\pi,\pi]
$$

### Метод

Коэффициенты Фурье вычислялись по формулам:

$$
a_0 = \frac{1}{\pi}\int_{-\pi}^{\pi} x(t)\,dt
$$

$$
a_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x(t)\cos(nt)\,dt
$$

$$
b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x(t)\sin(nt)\,dt
$$

Тригонометрический многочлен:

$$
S_N(t) = \frac{a_0}{2} + \sum_{n=1}^{N} \left(a_n \cos nt + b_n \sin nt\right)
$$

Подбиралась минимальная степень \(N\), при которой выполнялось условие:

$$
\|x - S_N\|_{L^2} < \varepsilon
$$

**Результат:** Построена тригонометрическая аппроксимация с заданной точностью.