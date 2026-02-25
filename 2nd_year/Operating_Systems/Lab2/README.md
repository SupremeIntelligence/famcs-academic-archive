# FAMCS OS Lab 2

## English Version

Implement a console application consisting of three threads: `main`, `min_max`, and `average`.

### Main thread (`main`) responsibilities:
1. Create an integer array, with size and elements entered from the console.
2. Create `min_max` and `average` threads.
3. Wait for both threads to finish execution.
4. Replace the minimum and maximum elements in the array with the arithmetic mean of the array.
5. Output the resulting array to the console.

### Min/Max thread (`min_max`) responsibilities:
- Find the minimum and maximum elements of the array.
- Output the results to the console.
- Sleep 7 milliseconds after each comparison.
- Finish execution.

### Average thread (`average`) responsibilities:
- Compute the arithmetic mean of the array elements.
- Output the result to the console.
- Sleep 12 milliseconds after each summation step.
- Finish execution.

---

## Русская версия

Задача. Написать программу для консольного процесса, который состоит из трёх потоков: `main`, `min_max` и `average`.

### Поток `main` должен выполнить следующие действия:
1. Создать массив целых чисел, размерность и элементы которого вводятся с консоли.
2. Создать потоки `min_max` и `average`.
3. Дождаться завершения потоков `min_max` и `average`.
4. Заменить максимальный и минимальный элементы массива на среднее значение элементов массива.
5. Вывести полученные результаты на консоль.

### Поток `min_max` должен выполнить следующие действия:
1. Найти минимальный и максимальный элементы массива и вывести их на консоль.
2. После каждого сравнения элементов «спать» 7 миллисекунд.
3. Завершить работу.

### Поток `average` должен выполнить следующие действия:
1. Найти среднее арифметическое значение элементов массива и вывести его на консоль.
2. После каждой операции суммирования элементов «спать» 12 миллисекунд.
3. Завершить работу.