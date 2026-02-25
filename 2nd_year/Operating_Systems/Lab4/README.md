# FAMCS OS Lab 4

## English Version

Implement a message-passing program between processes using a shared binary file. The program consists of one `Receiver` process and multiple `Sender` processes. `Sender` processes send messages to the `Receiver` process.

### Receiver process responsibilities:
1. Read from the console the name of the binary file and the number of entries in the file.
2. Create a binary file for messages (maximum message length: 20 characters).
3. Read from the console the number of `Sender` processes.
4. Launch the specified number of `Sender` processes, passing the file name as a command-line argument to each.
5. Wait for readiness signals from all `Sender` processes.
6. Repeatedly perform the following actions based on console commands:
   - Read a message from the binary file, or
   - Terminate the process.
> Note: If a read command is issued when the file is empty, the `Receiver` waits for a new message.

### Sender process responsibilities:
1. Open the shared binary file (file name provided via command-line argument).
2. Send a readiness signal to the `Receiver`.
3. Repeatedly perform the following actions based on console commands:
   - Send a message to the `Receiver`, or
   - Terminate the process.
> Note: If a write command is issued when the file is full, the `Sender` waits until space is available.  
Message length must be less than 20 characters.

### Additional requirements:
- Messages must be transmitted through the binary file as a FIFO circular queue.
- The `Receiver` must read messages in the order they were sent.
- **Simplified version**: implement for one `Receiver` and one `Sender` process. At any given time, only one message can be transmitted between them.

---

## Русская версия

Задача. Написать программу для передачи сообщений между процессами через общий бинарный файл. Программа включает один процесс `Receiver` и несколько процессов `Sender`. Процессы `Sender` посылают сообщения процессу `Receiver`.

### Процесс Receiver должен выполнять следующие действия:
1. Ввести с консоли имя бинарного файла и количество записей в файле.
2. Создать бинарный файл для сообщений (максимальная длина сообщения 20 символов).
3. Ввести с консоли количество процессов `Sender`.
4. Запустить заданное количество процессов `Sender`, передав каждому через командную строку имя файла.
5. Ждать сигнал на готовность к работе от всех процессов `Sender`.
6. Выполнять циклически следующие действия по команде с консоли:
   - Читать сообщение из бинарного файла, или
   - Завершить работу.
> Замечание: если вызывается команда чтения из пустого файла, процесс `Receiver` ожидает поступления нового сообщения.

### Процесс Sender должен выполнять следующие действия:
1. Открыть файл для передачи сообщений (имя файла получить из командной строки).
2. Отправить сигнал готовности процессу `Receiver`.
3. Выполнять циклически следующие действия по команде с консоли:
   - Отправить сообщение процессу `Receiver`, или
   - Завершить работу.
> Замечание: если вызывается команда записи в заполненный файл, процесс `Sender` ожидает пока появится место.  
Длина сообщения должна быть меньше 20 символов.

### Дополнительные требования:
- Передача сообщений через бинарный файл должна быть организована как кольцевая очередь FIFO.
- Процесс `Receiver` должен читать сообщения в порядке их отправления.
- **Упрощенный вариант**: реализовать для одного процесса `Receiver` и одного процесса `Sender`. В любой момент времени между процессами может передаваться только одно сообщение.