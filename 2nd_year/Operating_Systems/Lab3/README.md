# FAMCS OS Lab 3

## English Version

Implement a console application consisting of a `main` thread and multiple instances of a `marker` thread.

### Main thread (`main`) responsibilities:
1. Allocate memory for an integer array; the size is entered from the console.
2. Initialize all elements of the array to zero.
3. Ask for the number of `marker` threads to launch.
4. Start the specified number of `marker` thread instances, passing each its sequential number as a parameter.
5. Signal all `marker` threads to begin execution.
6. In a loop, perform the following actions:
   1. Wait until all `marker` threads signal that they cannot continue.
   2. Output the array contents to the console.
   3. Request the sequential number of the `marker` thread to be signaled for termination.
   4. Signal the chosen `marker` thread to terminate.
   5. Wait for the termination of the selected `marker` thread.
   6. Output the array contents to the console.
   7. Signal the remaining `marker` threads to continue execution.
7. Finish execution after all `marker` threads have terminated.

### Marker thread (`marker`) responsibilities:
1. Start execution upon receiving a signal from the `main` thread.
2. Initialize random number generation using `srand` with its sequential number as the seed.
3. Perform a cyclic operation in each iteration:
   1. Generate a random number using `rand`.
   2. Compute the index as the generated number modulo the array size.
   3. If the array element at this index is zero:
      - Sleep 5 milliseconds.
      - Set the element to its sequential number.
      - Sleep 5 milliseconds.
      - Continue to the next iteration.
   4. Otherwise:
      - Output the following information to the console:
        - Its sequential number
        - The count of elements it has marked
        - The index it could not mark
      - Signal the `main` thread that it cannot continue.
      - Wait for a signal from `main` to either continue or terminate.
4. Upon receiving a termination signal:
   - Reset all elements it marked to zero.
   - Terminate.
5. Upon receiving a continue signal, resume cyclic operation from step 3.

---

## Русская версия

Задача. Написать программу для консольного процесса, который состоит из потока `main` и нескольких экземпляров потока `marker`.

### Поток `main` должен выполнить следующие действия:
1. Захватить память под массив целых чисел, размерность которого вводится с консоли.
2. Инициализировать элементы массива нулями.
3. Запросить количество потоков `marker`, которые требуется запустить.
4. Запустить заданное количество экземпляров потока `marker`, передав каждому его порядковый номер.
5. Дать сигнал на начало работы всех потоков `marker`.
6. Выполнять в цикле следующие действия:
   1. Ждать, пока все потоки `marker` не подадут сигналы о невозможности продолжения работы.
   2. Вывести содержимое массива на консоль.
   3. Запросить порядковый номер потока `marker`, которому будет подан сигнал на завершение.
   4. Подать сигнал выбранному потоку `marker` на завершение работы.
   5. Дождаться завершения работы выбранного потока.
   6. Вывести содержимое массива на консоль.
   7. Подать сигнал оставшимся потокам `marker` на продолжение работы.
7. Завершить работу после того, как все потоки `marker` будут завершены.

### Поток `marker` должен выполнять следующие действия:
1. Начать работу по сигналу от потока `main`.
2. Инициализировать генерацию случайных чисел с помощью `srand`, передав свой порядковый номер как seed.
3. Циклически выполнять следующие действия:
   1. Сгенерировать случайное число с помощью `rand`.
   2. Вычислить индекс как остаток от деления на размер массива.
   3. Если элемент массива по этому индексу равен нулю:
      - Поспать 5 миллисекунд.
      - Записать в элемент массива свой порядковый номер.
      - Поспать 5 миллисекунд.
      - Продолжить цикл.
   4. В противном случае:
      - Вывести на консоль:
        - свой порядковый номер
        - количество помеченных элементов
        - индекс элемента, который невозможно пометить
      - Дать сигнал потоку `main` о невозможности продолжения работы.
      - Ждать сигнал от `main` на продолжение или завершение работы.
4. При получении сигнала на завершение:
   - Занулить все элементы массива, которые пометил.
   - Завершить работу.
5. При получении сигнала на продолжение работы возобновить цикл с пункта 3.