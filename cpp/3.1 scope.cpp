// 3.1 scope.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	int x = 3;
	cout << "X = " << x << endl;
	{
		int x = 4;
		int y = 7;
		cout << "X = " << x << " Y = " << y << endl;
	}
	cout << "X = " << x << endl;
    return 0;
}

