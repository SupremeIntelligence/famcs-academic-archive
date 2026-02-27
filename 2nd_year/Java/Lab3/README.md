# FAMCS Java Lab 3

## English Version

**Topic:** String Token Processing, Dates, Octal Numbers, and Formatting  

This lab demonstrates string parsing, tokenization, date and octal number detection, sorting, and formatting using Java.

---

## Task Description

Develop a console application that:

1. Reads input from a file (`input.txt`) and console:
   - First line: text containing tokens
   - Second line: separator characters

2. Splits the first line into tokens based on separators.

3. Processes each token:
   - Finds **octal numbers**
   - Finds **dates** in format `dd:MM:yy`
   - Inserts a random number after a detected date

4. Outputs:
   - Tokens found
   - List of octal numbers (before and after sorting)
   - List of dates (before and after sorting)

5. Performs number formatting:
   - Converts octal numbers to **currency** in a specified locale
   - Converts octal numbers to **percentages**

6. Removes the **shortest token** that starts with a digit and ends with a letter.

---

### Key Classes & Methods

- **`Java_Laba3`**
  - Main program logic: input, processing, output
  - Methods: `outputDates`, `outputOctNumbers`, `sortDates`, `sortNumbers`, `convertToCurrency`, `convertToPercents`, `removeElement`
  
- **`StringEditor`**
  - Tokenization: `Separate`
  - Octal numbers detection: `FindOctNumbs`
  - Date detection: `FindDate`
  - Random number insertion: `insertRandNumbAfterDate`
  - Shortest token identification: `indexOfShortestToken`

---

### Input & Output

- **Input:** `input.txt` and console for separator line and locale
- **Output:** `output.txt` and console
  - Found tokens
  - Octal numbers
  - Dates
  - Numbers formatted as currency and percentage
  - Modified string with inserted random number
  - Array of tokens with the shortest valid token removed

---

## Русская версия

**Тема:** Обработка строк, токенов, дат, восьмеричных чисел и форматирование  

Лабораторная работа демонстрирует разбор строк, выделение токенов, определение дат и восьмеричных чисел, сортировку и форматирование с помощью Java.

---

## Описание задания

Разработать консольное приложение, которое:

1. Считывает данные из файла (`input.txt`) и с консоли:
   - Первая строка: текст с токенами
   - Вторая строка: символы-разделители

2. Разбивает первую строку на токены по указанным разделителям.

3. Обрабатывает каждый токен:
   - Находит **восьмеричные числа**
   - Находит **даты** в формате `dd:MM:yy`
   - Вставляет случайное число после найденной даты

4. Выводит:
   - Найденные токены
   - Список восьмеричных чисел (до и после сортировки)
   - Список дат (до и после сортировки)

5. Форматирует числа:
   - Преобразует восьмеричные числа в **валюту** заданной локали
   - Преобразует восьмеричные числа в **проценты**

6. Удаляет **самый короткий токен**, начинающийся с цифры и оканчивающийся буквой.

---

### Основные классы и методы

- **`Java_Laba3`**
  - Логика программы: ввод, обработка, вывод
  - Методы: `outputDates`, `outputOctNumbers`, `sortDates`, `sortNumbers`, `convertToCurrency`, `convertToPercents`, `removeElement`
  
- **`StringEditor`**
  - Токенизация: `Separate`
  - Определение восьмеричных чисел: `FindOctNumbs`
  - Определение дат: `FindDate`
  - Вставка случайного числа: `insertRandNumbAfterDate`
  - Поиск самого короткого токена: `indexOfShortestToken`

---

### Ввод и вывод

- **Ввод:** `input.txt` и консоль для строки-разделителя и локали
- **Вывод:** `output.txt` и консоль
  - Найденные токены
  - Восьмеричные числа
  - Даты
  - Числа в формате валюты и процентов
  - Измененная строка со вставленным случайным числом
  - Массив токенов с удалением самого короткого корректного токена