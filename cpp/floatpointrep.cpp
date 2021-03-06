// floatpointrep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

void printbinary(char val)
{
	for (int i = 7; i >= 0; i--)
		if (val & (1 << i))
			cout << "1";
		else
			cout << "0";
}


int main()
{
	float f;
	cout << "Enter a number: ";
	cin >> f;
	char* pf = reinterpret_cast<char*>(&f);
	cout << "Your number in binary is ";
	for (int i = sizeof(float) - 1; i >= 0; i--) printbinary(pf[i]);
	cout << endl;
    return 0;
}