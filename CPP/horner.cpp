/*
 * horner.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

void drukujw(int st, float tbwsp[]) {
    ;
}

int main(int argc, char **argv)
{
    int stopien = 0;
    float x = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    float *tbwsp; // deklaracja wskaźnika, taka zmienna przechowująca adres komórki w pamięci
    tbwsp = new float [stopien + 1];
    for (int i = 0; i <= stopien; i++) {
        cout << "Podaj współczynnik przy potędze "
             << stopien - i << ": ";
        cin >> tbwsp[i];
    }
   
    cout << "Podaj argument: ";
    cin >> x;
   
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " " << "Wynosi: ";
    cout << endl;
   
    return 0;
}


}



