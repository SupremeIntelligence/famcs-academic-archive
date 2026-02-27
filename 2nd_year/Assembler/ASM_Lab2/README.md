# FAMCS ASM Lab 2

## English Version

**Topic** Array Rearrangement  

**Objective:**  
Rearrange an integer array `A = (a_i), i=1..n, n<=100` so that:  

- Positive numbers come first, then negative numbers  
- Within positive and negative parts, even and odd numbers alternate  

**Implementation:**  

- **C++**: Initializes the array with random non-zero integers (`-50..49`), allocates auxiliary arrays for positive, negative, even, and odd numbers.  
- **ASM block**:  
  - Separates array into positive and negative numbers  
  - Further splits positives and negatives into even and odd numbers  
  - Merges back into the original array in the required alternating order  

**Output:**  

- Prints the original unsorted array  
- Prints the sorted array with the specified arrangement  

---

## Sample Run
```
Enter array size (<=100): 10
Original array:
23 -12 7 4 -5 10 -8 15 2 -3
Sorted array:
4 7 10 23 2 15 -12 -5 -8 -3
```
---

## Русская версия

**Тема:** Перестановка элементов массива  

**Цель:**  
Переставить элементы массива `A = (a_i), i=1..n, n<=100` так, чтобы:  

- Сначала шли положительные числа, потом отрицательные  
- В пределах положительных и отрицательных чередовались чётные и нечётные числа  

**Реализация:**  

- **C++**: Генерация случайных чисел (`-50..49`), выделение вспомогательных массивов для положительных, отрицательных, чётных и нечётных чисел  
- **ASM блок**:  
  - Разделение массива на положительные и отрицательные числа  
  - Деление на чётные и нечётные  
  - Сборка массива в требуемом порядке  

**Вывод:**  

- Неотсортированный массив  
- Отсортированный массив с чередованием элементов  

---

## Пример работы

```
Введите размер массива (<=100): 10
Неотсортированный массив:
23 -12 7 4 -5 10 -8 15 2 -3
Отсортированный массив:
4 7 10 23 2 15 -12 -5 -8 -3
```
