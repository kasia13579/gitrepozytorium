/*
 * szyfr_cezara.cpp
 */


#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100

void szyfruj(int klucz, char tab[]) {
     klucz = klucz % 26;
    int kod = 0;
    int i = 0;
    while (tab[i] != '\0') {
        if (tab[i] == ' ') {
            i++;
            continue;
            }
        kod = (int)tab[i] + klucz;
        cout << (char)kod;
        i++;
        }
    }


int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;
    cout << "Podaj tekst:/n";
    cin.getline(tekst, MAKS);
    cout << cin.gcount() << endl;
    cout << strlen(tekst) << endl;
    return 0;
}
