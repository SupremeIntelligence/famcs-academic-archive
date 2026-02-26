# FAMCS OS Lab1

## English Version

**Topic:** Process Creation  

To develop a console application that demonstrates creation and synchronization of processes using system API functions.

---

## Task Description

Develop a console application consisting of three programs:

- `Main`
- `Creator` (utility program)
- `Reporter` (utility program)

---

### 1. Creator Utility

The `Creator` program:

- Receives from the command line:
  - Name of the binary file to create
  - Number of records to write
- Creates a binary file with records of the following structure:

```cpp
struct employee
{
    int num;        // employee ID
    char name[10];  // employee name
    double hours;   // worked hours
};
```

- Reads all record data from the console.
- Writes the records into the specified binary file.
- Terminates execution.

---

### 2. Reporter Utility

The `Reporter` program:

- Receives from the command line:
  1. Source binary file name
  2. Report file name
  3. Payment per hour

- Creates a text report file containing:
  1. Header:
     ```
     Report for file "<source binary file name>"
     ```
  2. Column titles:
     ```
     Employee ID | Name | Hours | Salary
     ```
  3. A sorted list of employees (sorted by employee ID), where:
     - Salary = hours × payment per hour

- Terminates execution after writing the report.

---

### 3. Main Program

The `Main` program performs the following steps:

1. Requests from console:
   - Binary file name
   - Number of records

2. Launches the `Creator` utility via command line, passing:
   - Binary file name
   - Number of records

3. Waits for `Creator` to finish using:

```cpp
WaitForSingleObject(hCreator, INFINITE);
```
4. Outputs the contents of the created binary file to the console.

5.	Requests from console:
    - Report file name
    - Payment per hour

6.	Launches the Reporter utility, passing:
    - Source binary file name
    - Report file name
    - Payment per hour

7.	Waits for Reporter to finish:
```cpp
WaitForSingleObject(hReporter, INFINITE);
```
8.	Outputs the generated report to the console.

9.	Terminates execution.

--- 

### Additional Requirement

To wait for process termination, use the Windows API function:

```cpp
DWORD WaitForSingleObject(
    HANDLE hHandle,
    DWORD dwMilliseconds
);
```
The second parameter must be set to INFINITE.

## Русская версия

**Тема:** Создание процессов  

**Цель:**  
Разработать консольное приложение, демонстрирующее создание и синхронизацию процессов с использованием системных API-функций.

---

## Описание задания

Разработать три программы:

- `Main`
- `Creator` (служебная программа)
- `Reporter` (служебная программа)

---

### 1. Утилита Creator

Программа `Creator`:

- Получает через командную строку:
  - Имя создаваемого бинарного файла
  - Количество записей
- Создает бинарный файл со следующей структурой записи:

```cpp
struct employee
{
    int num;        // идентификационный номер сотрудника
    char name[10];  // имя сотрудника
    double hours;   // количество отработанных часов
};
```
- Данные записей вводятся с консоли.
- Записывает данные в бинарный файл.
- Завершает работу.

---

### 2. Утилита Reporter

Программа `Reporter`:

- Получает через командную строку:
  1. Имя исходного бинарного файла
  2. Имя файла отчета
  3. Оплату за час работы

- Формирует текстовый отчет:
  1. Заголовок:
     ```
     Отчет по файлу "<имя исходного файла>"
     ```
  2. Строку заголовков:
     ```
     Номер | Имя | Часы | Зарплата
     ```
  3. Упорядоченный список сотрудников (по ID), где:
     - Зарплата = часы × оплата за час

- Завершает работу.

---

### 3. Программа Main

Программа `Main` выполняет:

1. Запрашивает с консоли:
   - Имя бинарного файла
   - Количество записей

2. Запускает `Creator`, передавая параметры через командную строку.

3. Ожидает завершения `Creator` с помощью:

```cpp
WaitForSingleObject(hCreator, INFINITE);
```

4.	Выводит содержимое бинарного файла на консоль.

5.	Запрашивает:
    - Имя файла отчета
    - Оплату за час работы
6.	Запускает Reporter, передавая параметры через командную строку.
7.	Ожидает завершения Reporter:
```cpp
WaitForSingleObject(hReporter, INFINITE);
```
8.	Выводит сформированный отчет на консоль.
9.	Завершает работу.

---

### Примечание:

Для ожидания завершения процессов использовать функцию:

```cpp
DWORD WaitForSingleObject(
    HANDLE hHandle,
    DWORD dwMilliseconds
);
```
Параметр dwMilliseconds установить равным INFINITE.