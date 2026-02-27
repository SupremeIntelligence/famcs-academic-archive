# FAMCS Java Lab 1

## English Version

**Topic:** Computing ln(1 − x) Using Taylor Series  

This lab demonstrates computation of the natural logarithm using Taylor series and Java's built-in `Math.log()` function for comparison. The program supports both simple data types and high-precision arithmetic.

---

## Task Description

Develop a console application to compute `ln(1-x)` using:

- Taylor series
- Java `Math.log()` for comparison

Supports two modes:

1. **Simple mode:** primitive types (`double`, `int`)  
2. **Big number mode:** high-precision (`BigDecimal`, `BigInteger`)  

---

### Main Class (`Java_Laba1`)

- Displays menu:
	1.	Simple data types
	2.	BigDecimal & BigInteger
	3.	Exit

- Reads input values
- Calls corresponding Taylor method
- Prints formatted results

---

### Taylor Series

```
ln(1 − x) = −x − x²/2 − x³/3 − …
```

- Precision: `ε = 10^(−k)`  
- Valid `x`: `−1 ≤ x < 1`  

**Outputs:**

- Taylor result vs `Math.log()`  
- Comparison of values  
- Octal & hexadecimal representation

---

### Input & Validation

- Methods: `Scanner` and `BufferedReader`  
- Re-prompts until valid input

---

### Unit Testing

- JUnit 5 tests (`TestTaylorClass.java`)  
- Verify `simpleTaylor` and `BigTaylor` accuracy within `ε`  
- Checks sample values and boundary cases

---

## Русская версия

**Тема:** Вычисление ln(1 − x) с помощью ряда Тейлора  

Лабораторная работа демонстрирует вычисление натурального логарифма с использованием ряда Тейлора и функции `Math.log()` для сравнения. Поддерживаются простые и высокоточные типы данных.

---

## Описание задания

Разработать консольное приложение для вычисления `ln(1 − x)` с использованием:

- ряда Тейлора
- функции Java `Math.log()` для сравнения

Режимы работы:

1. **Простой:** примитивные типы (`double`, `int`)  
2. **Высокая точность:** `BigDecimal` и `BigInteger`  

---

### Главный класс (`Java_Laba1`)

- Отображает меню:
	1.	Простые типы данных
	2.	BigDecimal & BigInteger
	3.	Выход

- Считывает данные с консоли
- Вызывает соответствующий метод Тейлора
- Выводит форматированные результаты

---

### Ряд Тейлора

```
ln(1 − x) = −x − x²/2 − x³/3 − …
```

- Точность: `ε = 10^(−k)`  
- Допустимые значения `x`: `−1 ≤ x < 1`  

**Вывод:**

- Результат ряда Тейлора и `Math.log()`  
- Сравнение значений  
- Восьмеричное и шестнадцатеричное представление

---

### Ввод и проверка данных

- Методы: `Scanner` и `BufferedReader`  
- Повторный запрос при некорректном вводе

---

### Модульное тестирование

- JUnit 5 (`TestTaylorClass.java`)  
- Проверка точности `simpleTaylor` и `BigTaylor` в пределах `ε`  
- Тестирование на примерах и граничных значениях

