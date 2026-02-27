# FAMCS ASM Lab 3

## English Version
 
**Topic:** C++ and ASM Calculation  

**Objective:**  
Compute the value of the function:  

\[
Y = \frac{-3x^3 + 5a*3 + x^3 - 2}{3x^2 - 7b / 7a + b}
\]

using both **C++** and **inline ASM**, including a call to an external `_stdcall` power function.

**Implementation:**  

- **C++ part:**  
  - Reads integers `a`, `b`, `x` from input  
  - Computes `Y` in pure C++ with `pow`  
  - Handles division by zero using `try-catch`  

- **ASM part:**  
  - Calculates numerator and denominator using registers  
  - Calls external `_stdcall` function `mypow` for exponentiation  
  - Performs integer division and stores the result  

**Output:**  

- Prints C++ computed result  
- Prints ASM computed result  

---

## Sample Run
```
Enter a, b, x:
2 3 4
C++ Result: 5
ASM Result: 5
```

---

## Русская версия

**Тема:** C++ + ASM вычисления  

**Цель:**  
Вычислить значение функции:  

\[
Y = \frac{-3x^3 + 5a*3 + x^3 - 2}{3x^2 - 7b / 7a + b}
\]

используя **C++** и **ASM**, включая вызов внешней функции `_stdcall` `mypow`.

**Реализация:**  

- **C++:**  
  - Ввод чисел `a`, `b`, `x`  
  - Вычисление `Y` в чистом C++  
  - Проверка деления на ноль с `try-catch`  

- **ASM:**  
  - Вычисление числителя и знаменателя в регистрах  
  - Вызов `_stdcall` функции `mypow` для возведения в степень  
  - Целочисленное деление и запись результата  

**Вывод:**  

- Результат C++  
- Результат ASM  

## Пример работы
```
Enter a, b, x:
2 3 4
C++ Result: 5
ASM Result: 5
```
