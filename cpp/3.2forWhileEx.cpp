// 3.2forWhileEx.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cstdlib>

using namespace std;


int main(int argx, char* argv[])
{
	int start = atoi(argv[1]);
	int bound = atoi(argv[2]);
	// Compute the sum with a for loop
	int sum = 0;
	for (int i = start; sum <= bound; i++)
		sum += 1;
	cout << "The sum from the for loop is " << sum << endl;
	// Compute the sume with a while loop
	sum = 0;
	int i = start;
	while (sum <= bound){
		sum += 1;
		i++;
	}
	cout << "The sum from the while loop is " << sum << endl;
    return 0;
}