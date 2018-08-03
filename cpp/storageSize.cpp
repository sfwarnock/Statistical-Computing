// storageSize.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	cout << "The storage allocated for a char is " << sizeof(char) << " bytes" << endl;
	cout << "The storage allocated for a an unsigned short integer is " << sizeof(unsigned short int) << " bytes" << endl;
	cout << "The storage allocated for an integer is " << sizeof(int) << " bytes" << endl;
	cout << "The storage allocated for a long integer is " << sizeof(long int) << " bytes" << endl;
	cout << "The storage allocated for an unsigned long integer is " << sizeof(unsigned long int) << " bytes" << endl;
	cout << "The storage allocated for a float is " << sizeof(float) << " bytes" << endl;
	cout << "The storage allocated for a double is " << sizeof(double) << " bytes" << endl;
	cout << "The storage allocated for a long double is " << sizeof(long double) << " bytes" << endl;
    return 0;
}