#include<iostream>
using namespace std;
extern "C" int _stdcall mypow(int value, int degree)
{
	return pow(value, degree);
}

int main()
{
	// Y=(-3x^3 +5a*3 +x^3 -2)/ (3x^2 Ц7b/7a )+b 
	int a, b, x;
	cout << "Enter a, b, x: \n";
	cin >> a >> b >> x;

	try
	{
		if (a == 0 || (3 * pow(x, 2) - 7 * b / (7 * a) + b) == 0)
		{
			throw "Division by zero";

		}
	}
	catch (const char* exception)
	{
		cout << exception << endl;
		return -1;
	}

	int y = (-3 * pow(x, 3) + 5 * a * 3 + pow(x, 3) - 2) / (3 * pow(x, 2) - 7 * b / (7 * a) + b);
	cout << "C++ Result: " << y << endl;

	int rez;
	int three = 3, seven = 7;
	_asm {
		mov eax, x

		push three
		push x
		call mypow

		imul eax, -3

		mov ebx, eax //сохран€ем значение в регистре ебх

		mov eax, 5
		imul eax, a
		imul  eax, three
		add ebx, eax //добавл€ем в ебх +5*3а

					
		push three
		push x
		call mypow 
					
		add ebx, eax

		sub ebx, 2

		mov eax, 2
		push eax
		push x
		call mypow

		imul eax, three
		
		mov ecx, eax //3x^2

		mov eax, 7
		imul b
		cdq
		idiv seven
		cdq
		idiv a

		sub ecx, eax

		add ecx, b

		mov eax, ebx
		cdq
		idiv ecx
		mov rez, eax

	}

	cout << "\n ASM Result: " << rez;

	return 0;
}