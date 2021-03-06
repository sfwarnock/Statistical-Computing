// 3.4 matrixPointer.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
using namespace std;

int main() {
	int nRows = 2, nCols = 3;
	double** pM = 0;
	pM = new double*[nRows];
	for (int i = 0; i < nRows; i++)
		pM[i] = new double[nCols];
	cout << "The value of pM is " << pM << endl;

	for (int i = 0; i < nRows; i++)
		cout << "The address for pM[" << i << "] is " << &pM[i] << endl;
	
	for (int i = 0; i < nRows; i++) {
		cout << "The value of pM[" << i << "] is " << pM[i] << endl;
		for (int j = 0; j < nCols; j++) {
			cout << "The addess of pM[" << i << "][" << j << "] is " << &pM[i][j] << endl;
		}
		cout << endl;
	}
	for (int i = 0; i < nRows; i++) {
		for (int j = 0; j < nCols; j++) {
			pM[i][j] = i * j;
			cout << "pM[" << i << "][" << j << "] = " << pM[i][j] << " ";
		}
		cout << endl;
	}
	// memory clean up
	for (int i = 0; i < nRows; i++)
		delete[] pM[i];
	delete[] pM;
	return 0;
}
