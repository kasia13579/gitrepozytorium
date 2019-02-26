/*
 * szyfr_przestawny.cpp
 */


#include <iostream>
#include <string.h> //strlen
using namespace std;

#define MAKS 100


void szyfruj(char tb[], int klucz){
    int ile = strlen(tb);

    
}


int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;

    cout << "Podaj tekst:\n";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(tekst, klucz);

    return 0;
}
