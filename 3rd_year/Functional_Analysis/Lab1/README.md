# FAMCS Functional Analysis & Integral Equations Lab1

## English Version

**Topic:** Iterative Methods for Nonlinear Equations, Linear Systems and Volterra Integral Equations
 
Implement numerical iterative methods for solving nonlinear equations, linear algebraic systems, and integral equations.

---

### Task 1 — Nonlinear Equation

Solve:

$$g(x) = x^7 + x^3 + 2x^2 + x − 1 = 0$$
on the interval [0, 1].

### Method

- Fixed-point iteration:
  
  $x_{n+1} = x_n − \lambda g(x_n)$

- Parameter:
  
  $\lambda = 2 / (g'(a) + g'(b))$

- A priori estimate of iterations
- Iteration until $|x_n − x_{n-1}| < \epsilon$
- Residual check |g(x*)|
- Graphical visualization of g(x)

**Result:** Root found with required accuracy.

---

### Task 2 — Linear System

Solve system:

$$Ax = B$$

### Method

- Reduction to normal equations:
  
  $A^TAx = A^TB$

- Iterative scheme:

  $x_{x+1} = Cx_n + D$

- Spectral estimate via maximum eigenvalue
- Convergence check using matrix norm
- A priori estimate of iterations

**Result:** Solution vector obtained with required precision.

---

### Task 3 — Volterra Integral Equation

Solve integral equation:

$$x(t) = 2t + 2 − \int_{0}^{t}x(s) ds$$

### Method

- Method of successive approximations
- Integral approximated numerically (cumulative sum)
- 2000 iterations performed
- Graph of solution plotted

**Result:** Numerical approximation of solution obtained.

---

## Русская версия

**Тема:** Итерационные методы решения нелинейных уравнений, систем линейных уравнений и интегральных уравнений Вольтерра

Реализация численных итерационных методов для решения нелинейных уравнений, систем линейных алгебраических уравнений и интегральных уравнений.

---

### Задание 1 — Нелинейное уравнение

Решить уравнение:

$$g(x) = x^7 + x^3 + 2x^2 + x − 1 = 0$$

на отрезке [0, 1].

### Метод

- Метод простой итерации:

  $x_{n+1} = x_n − \lambda g(x_n)$

- Параметр:

  $\lambda = 2 / (g'(a) + g'(b))$

- Априорная оценка числа итераций
- Итерации до выполнения условия $|x_n − x_{n-1}| < \epsilon$
- Проверка невязки $|g(x^*)|$
- Графическая визуализация функции $g(x)$

**Результат:** Корень найден с заданной точностью.

---

### Задание 2 — Система линейных уравнений

Решить систему:

$$Ax = B$$

### Метод

- Приведение к нормальным уравнениям:

  $A^TAx = A^TB$

- Итерационная схема:

  $x_{n+1} = Cx_n + D$

- Спектральная оценка через максимальное собственное значение
- Проверка условия сходимости по норме матрицы
- Априорная оценка числа итераций

**Результат:** Получен вектор решения с требуемой точностью.

---

### Задание 3 — Интегральное уравнение Вольтерра

Решить интегральное уравнение:

$$x(t) = 2t + 2 − \int_{0}^{t}x(s) ds$$

### Метод

- Метод последовательных приближений
- Численное приближение интеграла (накопленная сумма)
- Выполнено 2000 итераций
- Построен график решения

**Результат:** Получено численное приближение решения.