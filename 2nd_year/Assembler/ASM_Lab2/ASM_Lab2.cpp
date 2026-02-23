#include <iostream>
#include<time.h>
using namespace std;

int main()
{
    /*Поместить в последовательности A=(ai), i=1..n , n<=100, четные элементы, по очереди (через один) с нечётными. В начале массива-положительные числа, затем отрицательные
    */
    setlocale(LC_ALL, "RUS");
    int* mas;
    int size;
    do
    {
        cout << "Введите размерность массивa до 100:\t";
        cin >> size;
    } while (size > 100);

    mas = new int[size];
    cout << "\nНеотсортированный массив:\n";
    srand(time(NULL));
    for (int i = 0; i < size; i++)
    {
        do {
            mas[i] = rand() % 100 - 50;
        } while (mas[i] == 0);
        cout << mas[i] << " ";
    }
    int m_counter = size;
    int tempsize = size;
    int pos_size = 0;
    int neg_size = 0;
    int even_size = 0;
    int odd_size = 0;
    int* pos_numbers = new int[size];
    int* neg_numbers = new int[size];
    int* even = new int[size];
    int* odd = new int[size];

    int temp = 4;
    _asm
    {
        mov ebx, mas
        mov ecx, m_counter
        mov esi, pos_numbers
        mov edi, neg_numbers
        //разделяем массив на положительные и отрицательные
        separation :
        mov eax, [ebx]
            cmp eax, 0
            jg positive
            jle negative

            positive :
        mov[esi], eax
            add esi, 4
            inc pos_size
            jmp next1

            negative :
        mov[edi], eax
            add edi, 4
            inc neg_size

            next1 :
        add ebx, 4
            loop separation

            //разделяем положительный массив на четные и нечетные
            mov ebx, pos_numbers
            mov esi, even
            mov edi, odd
            mov ecx, pos_size

            sort1 :
        mov eax, [ebx]
            test eax, 01
            jz Even1
            jnz Odd1

            Even1 :
        mov[esi], eax
            add esi, 4
            inc even_size
            jmp next2

            Odd1 :
        mov[edi], eax
            add edi, 4
            inc odd_size

            next2 :
        add ebx, 4
            loop sort1

            //заполняем массив чередующимися положительными четными и нечетными
            mov edi, mas
            mov esi, even
            mov ecx, even_size
            mov ebx, even_size
            mov edx, odd_size
            sub ebx, edx
            merge1Even :

        mov eax, [esi]
            mov[edi], eax
            add edi, 4

            cmp ecx, ebx

            jle EvenGreater1
            add edi, 4

            EvenGreater1:
        add esi, 4

            loop merge1Even


            mov edi, mas  //заполняем нечетными положительными
            mov esi, odd
            mov ecx, odd_size
            add edi, 4    //начиная со второго элемента

            mov ebx, odd_size
            mov edx, even_size
            sub ebx, edx
            inc ebx

            merge1Odd :
        mov eax, [esi]
            mov[edi], eax
            add edi, 4

            cmp ecx, ebx

            jle OddGreater1
            add edi, 4

            OddGreater1:
        add esi, 4


            loop merge1Odd

            //разделяем отрицательные на четные и нечетные
            mov even_size, 0
            mov odd_size, 0

            mov ebx, neg_numbers
            mov esi, even
            mov edi, odd
            mov ecx, neg_size

            sort2 :
        mov eax, [ebx]
            test eax, 01
            jz Even3
            jnz Odd3

            Even3 :
        mov[esi], eax
            add esi, 4
            inc even_size
            jmp next3

            Odd3 :
        mov[edi], eax
            add edi, 4
            inc odd_size

            next3 :
        add ebx, 4
            loop sort2

            //заполняем массив чередующимися отрицательными четными и нечетными
            mov edi, mas
            mov esi, even
            mov ecx, even_size

            mov eax, pos_size
            imul temp
            add edi, eax

            mov ebx, even_size
            mov edx, odd_size
            sub ebx, edx

            merge2Even : //заполняем четными отриц

        mov eax, [esi]
            mov[edi], eax
            add edi, 4

            cmp ecx, ebx

            jle EvenGreater2
            add edi, 4

            EvenGreater2:
        add esi, 4


            loop merge2Even


            mov edi, mas  //заполняем нечетными отриц
            mov esi, odd
            mov ecx, odd_size
            add edi, 4    //начиная со второго элемента

            mov eax, pos_size
            imul temp
            add edi, eax

            mov ebx, odd_size
            mov edx, even_size
            sub ebx, edx
            inc ebx

            merge2Odd :
        mov eax, [esi]
            mov[edi], eax
            add edi, 4

            cmp ecx, ebx

            jle OddGreater2
            add edi, 4

            OddGreater2:
        add esi, 4


            loop merge2Odd
    }

    cout << "\nОтсортированный массив:\n";
    for (int i = 0; i < size; i++)
    {
        cout << mas[i] << "  ";
    }

    delete[]mas;
    delete[]pos_numbers;
    delete[]neg_numbers;
    delete[]even;
    delete[]odd;
}