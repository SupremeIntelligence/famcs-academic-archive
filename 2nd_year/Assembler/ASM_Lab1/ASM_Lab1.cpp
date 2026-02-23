#include<iostream>
using namespace std;
extern "C" int CALC(int a, int b, int x);
int main()
{
	// Y=(-3x^3 +5a*3 +x^3 -2)/ (3x^2 –7b/7a )+b 
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

	int rez = CALC(a, b, x);
	int three = 3, seven = 7;


	cout << "\n ASM Result: " << rez;

	return 0;
}