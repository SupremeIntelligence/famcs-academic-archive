# FAMCS ASM Lab 1

## English Version

**Topic:** Mixed C++ and Assembly Calculation  

**Objective:**  
Develop a program that calculates a mathematical expression using both C++ and inline/linked Assembly routines, demonstrating integration between C++ and Assembly.

---

## Task Description

Create a console application that:

1. Reads three integer values from the console: `a`, `b`, `x`.
2. Computes the expression `Y = (-3x^3 + 5a*3 + x^3 - 2) / (3x^2 - 7b/(7a) + b)`
3. Performs the calculation in two ways:
   - Using C++ arithmetic.
   - Using an external Assembly procedure `CALC`.
4. Handles division by zero via a C++ exception.

---

## Implementation Details

- **C++ Program (`ASM_Lab1.cpp`)**:
  - Reads user input.
  - Checks for division by zero and throws an exception if necessary.
  - Calculates the result in C++.
  - Calls the external Assembly procedure `CALC`.
  - Prints both C++ and ASM results to the console.

- **Assembly Procedure (`ASM_Laba1-3.asm`)**:
  - Uses MASM syntax (`.586`, `.MODEL FLAT, C`).
  - Implements `CALC` procedure:
    - Computes numerator and denominator separately.
    - Uses integer arithmetic with `imul`, `idiv`.
    - Returns result in `EAX`.

- **Integration**:
  - Assembly routine is linked as an external function (`extern "C"`) in the C++ code.

---

## Sample Run
```
Enter a, b, x:
2 3 1
C++ Result: 2
ASM Result: 2
```
---

## Notes

- Ensure that the Assembly procedure is correctly linked to the C++ project.
- Exception handling in C++ prevents runtime errors for division by zero.
- Integer arithmetic in Assembly may differ slightly from floating-point C++ results if using large numbers.

---

## Русская версия

**Тема:** Смешанные вычисления C++ и Assembly  

**Цель:**  
Разработать программу, которая вычисляет математическое выражение с использованием как C++, так и внешней процедуры на Assembly, демонстрируя интеграцию C++ и Assembly.

---

## Описание задания

Создать консольное приложение, которое:

1. Считывает три целых числа с консоли: `a`, `b`, `x`.
2. Вычисляет выражение `Y = (-3x^3 + 5a*3 + x^3 - 2) / (3x^2 - 7b/(7a) + b)`
3. Вычисляет результат двумя способами:
   - на C++;
   - с помощью внешней процедуры Assembly `CALC`.

4. Обрабатывает деление на ноль через исключение C++.

---

## Реализация

- **C++ программа (`ASM_Lab1.cpp`)**:
  - Чтение входных данных.
  - Проверка деления на ноль и генерация исключения.
  - Вычисление результата на C++.
  - Вызов процедуры Assembly `CALC`.
  - Вывод результатов на экран.

- **Процедура Assembly (`ASM_Laba1-3.asm`)**:
  - Синтаксис MASM (`.586`, `.MODEL FLAT, C`).
  - Реализует `CALC`:
    - Отдельное вычисление числителя и знаменателя.
    - Использование целочисленной арифметики (`imul`, `idiv`).
    - Возврат результата в регистре `EAX`.

- **Интеграция**:
  - Вызов внешней функции через `extern "C"` в C++.

---

## Пример работы
```
Введите a, b, x:
2 3 1
Результат C++: 2
Результат ASM: 2
```
---

## Примечания

- Убедитесь, что процедура Assembly правильно связана с проектом на C++.
- Обработка исключений предотвращает ошибки деления на ноль.
- Целочисленные вычисления в ASM могут немного отличаться от C++ при больших числах.