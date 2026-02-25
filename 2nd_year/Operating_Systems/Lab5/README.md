# FAMCS OS Lab 5

## English Version

**Topic:** "Data exchange using named pipes"  
Implement a program to manage parallel process access to a file via named pipes.

### Server process responsibilities:
1. Create a binary file with records of the following structure:

```cpp
struct employee
{
    int num;       // employee ID
    char name[10]; // employee name
    double hours;  // worked hours
};
```

2. File name and employee data are entered from the console.
3. Output the created file to the console.
4. Launch Client processes that access the file via named pipes. Number of clients is entered from the console.
5. Serve client requests as follows:
    - If a client requests to modify a record, that record is locked for other clients until modification is complete.
    - If a client requests to read a record:
    - Multiple clients can read the same record concurrently.
    - Writing access by other clients is blocked until all reads are finished.
6. After all clients finish, output the modified file to the console.
7. Terminate the server process via console command.

### Client process responsibilities:
1.  Execute a loop:
    - Request one of the following operations from the console:
    - Modify a record
    - Read a record
    - Exit
    - Perform the selected operation after entering necessary data.
2. Access records by employee ID.
3. For modification:
    1.	Request the record key (ID) from the console.
    2.	Send a request to the server.
    3.	Display the record received from the server.
    4. Enter new field values.
    5. Send the modified record to the server.
    6. End access to the record.
4. For reading:
    1.	Request the record key (ID).
    2.	Send request to the server.
    3.	Display the received record.
    4.	End access to the record.

--- 

## Русская версия

**Тема**: “Обмен данными по именованным каналам”
Написать программу для управления доступом параллельных процессов к файлу через именованные каналы.

### Процесс-сервер:
1.	Создать бинарный файл с записями следующей структуры:

```cpp
struct employee
{
    int num;       // идентификационный номер сотрудника
    char name[10]; // имя сотрудника
    double hours;  // количество отработанных часов
};
```

2.	Имя файла и данные сотрудников вводятся с консоли.
3.	Вывести созданный файл на консоль.
4.	Запустить процессы Client, которые получают доступ к файлу по именованным каналам. Количество процессов вводится с консоли.
5.	Обслуживать запросы клиентов:
    - Если клиент запрашивает изменение записи, запись блокируется для других клиентов до завершения модификации.
    - Если клиент запрашивает чтение записи:
    - Несколько клиентов могут читать запись одновременно.
    - Доступ на запись другими клиентами блокируется до окончания чтения.
6.	После завершения работы всех клиентов вывести модифицированный файл на консоль.
7.	Завершить работу сервера по команде с консоли.

### Процесс-клиент Client:
1.	Выполнять цикл:
    - Запросить с консоли выполнение операции:
    - Модификация записи
    - Чтение записи
    - Выход
    - Выполнить выбранную операцию после ввода необходимых данных.
2.	Доступ к записи осуществляется по ID сотрудника.
3.	Для модификации записи:
    1.	Запросить ключ записи (ID).
    2.	Послать запрос серверу.
    3.	Вывести полученную запись на консоль.
    4.	Ввести новые значения полей.
    5.	Послать изменённую запись серверу.
    6.	Завершить доступ к записи.
4.	Для чтения записи:
    1.	Запросить ключ записи (ID).
    2.	Послать запрос серверу.
    3.	Вывести запись на консоль.
    4.	Завершить доступ к записи.
