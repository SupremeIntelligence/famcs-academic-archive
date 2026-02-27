# FAMCS Assembly Programming Course

## English Version

**Course:** Assembly Programming  

**Objective:**  
Study low-level programming principles, computer architecture basics, and integration of Assembly with C/C++ applications.

---

## Course Content

The course includes theoretical material and practical labs covering:

1. **x86 Architecture Basics**
   - Registers (EAX, EBX, ECX, EDX, etc.)
   - Stack and memory model
   - Addressing modes

2. **Arithmetic and Logic Instructions**
   - `mov`, `add`, `sub`
   - `imul`, `idiv`
   - `test`, `cmp`
   - Conditional and unconditional jumps

3. **Control Flow**
   - Loops (`loop`, conditional jumps)
   - Branching logic

4. **Procedures**
   - PROC / ENDP
   - Calling conventions (`C`, `_stdcall`)
   - Passing parameters via stack
   - Returning values in registers

5. **Inline Assembly in C++**
   - `_asm` blocks
   - Register manipulation
   - Integration with C++ variables

6. **Mixed C++ and ASM Projects**
   - External ASM procedures
   - Linking `.asm` files with C++ projects
   - Calling C++ functions from Assembly

7. **Array and Memory Manipulation**
   - Working with pointers
   - Dynamic memory
   - Element rearrangement algorithms

---

## Lab Structure

Each lab includes:

- **Task Description**
- **Mathematical or Algorithmic Problem**
- **Implementation in ASM or C++ + ASM**
- **Console Input/Output**
- **Comparison with C++ Implementation (if applicable)**

---

## Implemented Labs

- **Lab 1** – Expression evaluation using external ASM procedure  
- **Lab 2** – Array rearrangement using inline ASM  
- **Lab 3** – Expression evaluation using inline ASM and `_stdcall` function calls  

---

## Skills Acquired

- Understanding low-level computation
- Manual arithmetic and register management
- Stack-based parameter passing
- Interfacing Assembly with C++
- Debugging low-level code

---

## Русская версия

**Курс:** Ассемблерное программирование  

**Цель:**  
Изучение принципов низкоуровневого программирования, архитектуры компьютера и интеграции Assembly с C/C++.

---

## Содержание курса

Курс включает теорию и лабораторные работы по следующим темам:

1. **Архитектура x86**
   - Регистры (EAX, EBX, ECX, EDX и др.)
   - Стек и модель памяти
   - Способы адресации

2. **Арифметические и логические инструкции**
   - `mov`, `add`, `sub`
   - `imul`, `idiv`
   - `test`, `cmp`
   - Условные и безусловные переходы

3. **Управление выполнением**
   - Циклы (`loop`)
   - Условные переходы

4. **Процедуры**
   - PROC / ENDP
   - Соглашения о вызовах (`C`, `_stdcall`)
   - Передача параметров через стек
   - Возврат значения через регистры

5. **Inline ASM в C++**
   - Блоки `_asm`
   - Работа с регистрами
   - Взаимодействие с переменными C++

6. **Смешанные проекты C++ + ASM**
   - Внешние ASM-процедуры
   - Линковка `.asm` с C++
   - Вызов функций C++ из Assembly

7. **Работа с массивами и памятью**
   - Указатели
   - Динамическая память
   - Алгоритмы перестановки элементов

---

## Структура лабораторных работ

Каждая лабораторная включает:

- Описание задания  
- Реализацию на ASM или C++ + ASM  
- Консольный ввод/вывод  
- Сравнение с реализацией на C++ (при необходимости)  

---

## Реализованные лабораторные

- **ЛР1** – Вычисление выражения через внешнюю ASM-процедуру  
- **ЛР2** – Перестановка элементов массива через inline ASM  
- **ЛР3** – Вычисление выражения через inline ASM с вызовом `_stdcall` функции  

---

## Приобретённые навыки

- Понимание низкоуровневых вычислений  
- Работа с регистрами  
- Передача параметров через стек  
- Интеграция Assembly и C++  
- Отладка низкоуровневого кода  