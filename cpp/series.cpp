// series.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
	float sumL = 0., sumU = 0.;
	int n = atoi(argv[1]);
	for (int j = 1; j <= n; j++)
	{
		sumL = sumL + 1 / (float)(j*j);
		sumU = sumU + 1 / (float)((n + 1 - j) * (n + 1 - j));
	}
	cout << setprecision(8) << "Direct and reverse sums are " << sumL << " and " << sumU << endl;
    return 0;
}