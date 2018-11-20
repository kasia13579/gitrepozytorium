/*
 * horner.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

void drukujw(int st, float tbwsp[]) {
    int i = 0;
    for (i = 0; i < st; i++) {
        cout << tbwsp[i] << "x^" << st-i << " + ";
    }
    cout << tbwsp[i] << endl;
}

float horner_it(int st, float tbwsp[], float x) {
    // 0, 1, 2, 3
    // x (x (2x + 3) + 5) + 4
    float wynik = tbwsp[0];
    for (int i = 1; i < st+1; i++) {
        wynik = wynik * x + tbwsp[i];
    }
    return wynik;
}


int main(int argc, char **argv)
{
    int stopien = 0;
    float x = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    float *tbwsp;  //wskaźnik - przechowuje adres komórki w pamięci
    tbwsp = new float [stopien+1];
    for (int i=0; i <= stopien; i++) {
        cout << "Podaj współczynnik przy potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
    }
    cout << "Podaj argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " wynosi: " << horner_it(stopien, tbwsp, x);
    cout << endl;
    
	return 0;
}


