// binaryRep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

void printBinary(unsigned short val);

int main()
{	
	unsigned short inVal;
	cout << "Enter a number between 0 and 65535: ";
	cin >> inVal;
	cout << "Your number in binary is ";
	printBinary(inVal);
	cout << endl;
    return 0;
}

void printBinary(unsigned short val)
{
	for (int i = 15; i >= 0; i--)
		if (val & (1 << i))
			cout << "1";
		else
			cout << "0";
}