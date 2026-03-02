# FAMCS Functional Analysis & Integral Equations Lab3

## English Version

**Topic:** Orthogonal Approximation of Functions in Different Bases

Implementation of function approximation methods using Legendre polynomials, Chebyshev polynomials of the first kind, and trigonometric basis functions.

---

### Task 1 — Legendre Polynomial Approximation

Approximate the function

$$
x(t) = 2|t| - t, \quad t \in [-1,1]
$$

### Method

Legendre polynomials $P_k(t)$ were used as an orthogonal basis.

The Fourier–Legendre coefficients were computed as:

$$
C_k = \frac{2k+1}{2} \int_{-1}^{1} x(t) P_k(t)\,dt
$$

The approximation was constructed using polynomials up to degree 3 and transformed into power form.

The mean-square error was computed as:

$$
\|x - S\|_{L^2}^2 =
\int_{-1}^{1} (x(t) - S(t))^2 dt
$$

**Result:** A third-degree polynomial approximation was obtained.

---

### Task 2 — Chebyshev Polynomial Approximation (First Kind)

Approximate the function

$$
x(t) = t \sin^2\left(\frac{t}{2}\right), \quad t \in [-1,1]
$$

### Method

Chebyshev polynomials of the first kind were used:

$$
T_k(t) = \cos(k \arccos t)
$$

The coefficients were computed as:

$$
C_0 = \frac{1}{\pi} \int_{-1}^{1}
\frac{x(t)}{\sqrt{1-t^2}} dt
$$

$$
C_k = \frac{2}{\pi} \int_{-1}^{1}
\frac{x(t) T_k(t)}{\sqrt{1-t^2}} dt
$$

A polynomial approximation of degree $\le 5$ was constructed.

The following errors were evaluated:

$$
\|x - S\|_{L^2}
$$

and

$$
\|x - S\|_{\infty}
$$

**Result:** An orthogonal approximation in the Chebyshev basis was obtained.

---

### Task 3 — Trigonometric Approximation (Fourier Series)

Approximate the function

$$
x(t) = 2t - t^2, \quad t \in [-\pi,\pi]
$$

### Method

Fourier coefficients were computed as:

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} x(t)\,dt
$$

$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x(t)\cos(nt)\,dt
$$

$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x(t)\sin(nt)\,dt
$$

The trigonometric polynomial was constructed as:

$$ S_N(t) = \frac{a_0}{2} + \sum_{n=1}^{N} \left(a_n \cos nt + b_n \sin nt \right)$$

The minimal degree $N$ was selected such that

$$
\|x - S_N\|_{L^2} < \varepsilon
$$

**Result:** A trigonometric approximation satisfying the required accuracy was obtained.

---

## Русская версия

**Тема:** Ортогональная аппроксимация функций в различных базисах

Реализация методов аппроксимации функций с использованием многочленов Лежандра, Чебышева первого рода и тригонометрического базиса.

---

### Задание 1 — Аппроксимация многочленами Лежандра

Аппроксимировать функцию

$$
x(t) = 2|t| - t, \quad t \in [-1,1]
$$

### Метод

Использовались многочлены Лежандра $P_k(t)$.

Коэффициенты Фурье–Лежандра вычислялись по формуле:

$$
C_k = \frac{2k+1}{2} \int_{-1}^{1} x(t) P_k(t)\,dt
$$

Аппроксимация строилась в виде линейной комбинации многочленов до степени 3 и приводилась к степенной форме.

Среднеквадратичная погрешность:

$$
\|x - S\|_{L^2}^2 =
\int_{-1}^{1} (x(t) - S(t))^2 dt
$$

**Результат:** Получена полиномиальная аппроксимация степени 3.

---

### Задание 2 — Аппроксимация многочленами Чебышева I рода

Аппроксимировать функцию

$$
x(t) = t \sin^2\left(\frac{t}{2}\right), \quad t \in [-1,1]
$$

### Метод

Использовались многочлены Чебышева первого рода:

$$
T_k(t) = \cos(k \arccos t)
$$

Коэффициенты вычислялись по формулам:

$$
C_0 = \frac{1}{\pi} \int_{-1}^{1}
\frac{x(t)}{\sqrt{1-t^2}} dt
$$

$$
C_k = \frac{2}{\pi} \int_{-1}^{1}
\frac{x(t) T_k(t)}{\sqrt{1-t^2}} dt
$$

Построена аппроксимация степени $\le 5$.

Вычислены погрешности:

$$
\|x - S\|_{L^2}
$$

и

$$
\|x - S\|_{\infty}
$$

**Результат:** Получена ортогональная аппроксимация в базисе Чебышева.

---

### Задание 3 — Тригонометрическая аппроксимация (ряд Фурье)

Аппроксимировать функцию

$$
x(t) = 2t - t^2, \quad t \in [-\pi,\pi]
$$

### Метод

Коэффициенты Фурье:

$$
a_0 = \frac{1}{\pi} \int_{-\pi}^{\pi} x(t)\,dt
$$

$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x(t)\cos(nt)\,dt
$$

$$
b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x(t)\sin(nt)\,dt
$$

Тригонометрический многочлен:

$$ S_N(t) = \frac{a_0}{2} + \sum_{n=1}^{N} \left(a_n \cos nt + b_n \sin nt \right)$$

Подбиралась минимальная степень $N$, при которой

$$
\|x - S_N\|_{L^2} < \varepsilon
$$

**Результат:** Построена тригонометрическая аппроксимация с заданной точностью.