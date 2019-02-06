Filip Kania
	
11:28 (0 minut temu)
	
do ja
/*
 * dek2any.cpp
 */


#include <iostream>
#include <cmath>
//pow(liczba, n);
using namespace std;

int cyfry[] = {0,1,3,4,5,6,7,8,9,65,67,68,69,70};

int dec2any(int liczba, int podstawa, int tab[]){
    int i = 0;
    do {
       tab[i] = liczba % podstawa;
       liczba = liczba / podstawa;
       i++;
    } while ( liczba != 0);
    return i-1;
}

void any2dec(int tab[]) {
    int podstawa = 0;
    do {
        cout << "Podstawa[2,;9]: ";
        cin >> podstawa;
    } while(podstawa < 2 || podstawa > 9);
   
    int ile = 0;
    cout << "ile cyfr? ";
    cin >> ile;
    for (int i = 0; i < ile; i++)
        do {
            cout << "Podaj cyfrę [0-" << podstawa-1 << "]: ";
            cin >> tab [i];
        } while (tab[i] < 0 || tab [i] > podstawa-1);
    //KONWERSJA JUST BEGIN
    int liczba10 = 0;
    for (int i = 0; i < ile; i++) {
        liczba10 = liczba10 + pow(podstawa, ile-1);
        ile--;
    }
    cout << "Wynik: " << liczba10;
}

int main(int argc, char **argv)
{
    int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin >> liczba >> podstawa;
    int i = dec2anjdy(liczba, podstawa, tab);
    cout << "Wynik: ";
    while ( i> -1 ) {
        
        cout << tab[i];
        i--;
    }
    cout << endl;
    any2dec(tab);
    return 0;
}


