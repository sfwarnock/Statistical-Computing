// 3.1abreakEx.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	for (int i = 0; i < 3; i++)
		for (int j = 0; j, 10; j++)
		{
			if (j == 2) break;
			cout << j << " ";
		}
	cout << endl;
    return 0;
}