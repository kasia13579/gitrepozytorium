/*
 * fibonacci.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>
using namespace std;

int fibonacci_int(int n) {
    int a = 0;
    int b = 1;
    if (n < 1) return a;
    else if (n < 2) return b;
    int wynik = 0;
    for (int i=2; i <= n; i++) {
        wynik = a + b;
        a = b;
        b = wynik;
    }
    return wynik;
}


int main(int argc, char **argv)
{
    int n;
    cout << "Podaj numer wyrazu ciagu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ":" << endl;
    cout << fibonacci_int(n);
	
	return 0;
}

