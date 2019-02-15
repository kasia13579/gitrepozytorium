/*
 * dec2bin.cpp
 * 
<<<<<<< HEAD
=======
 * Program zamienia liczbę dziesiętną podaną przez użytkownika na binarną
>>>>>>> ebdf89c047a3eece0a19b761bab6fed4fe688087
 */

#include <iostream>
#include <cmath>

using namespace std;

<<<<<<< HEAD
int cyfry[16] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 65, 66, 67, 68, 69, 70}

int dec2any(int liczba, int podstawa, int tab[]) {
    int i=0;
    do {
        tab[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++;
    } while (liczba != 0);

    return i-1;
}

void any2dec(int tab[]) {
    int podstawa = 0;
    do {
        cout << "Podstawa <2;9>: ";
        cin >> podstawa;
    } while (podstawa < 2 || podstawa > 9);
    
    int ile = 0;
    cout << "Ile cyfr? "; cin >> ile;
    for(int i = 0; i < ile; i++)
        do {
            cout << "Podaj cyfrę (0-" << podstawa-1 << "): ";
            cin >> tab[i];
        } while (tab[i]<0 || tab[i]>podstawa-1);
    // konwersja na system dziesiętny
    int liczba10 = 0;
    for (int i=0; i < ile; i++) {
        // kolejna cyfra z tabeli mnożona przez odpowiednią potęgę podstawy;
        // pow(liczba, potega)
        liczba10 += tab[i] * pow(podstawa, ile-1-i);
    }
    cout << "Wynik: " << liczba10;
}

int main(int argc, char **argv)
{
    int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego:\n";
    cin >> liczba >> podstawa;
    int i = dec2any(liczba, podstawa, tab);
    cout << "Wynik: ";
    while (i >= 0) {
        if (podstawa > 9)
            cout << cyfry[tab[i]];
        else
            cout << tab[i];
        i--;
    }
    cout << endl;
    any2dec(tab);
    return 0;
}
=======
int dec2bin(int ld)
{
    int lbin = 0;
    int i = 1;
    
    while (ld > 0)
    {
        lbin += (ld%2)*i;
        ld /= 2;
        i *= 10;
    }
    return lbin;
}

void dec2bin(int ld)
{
    int i = 0;
    int tab[8];

	while(ld > 0)
	{
		tab[i++]=ld%2;
		ld/=2;
	}

	for(int j=i-1;j>=0;j--)
		cout<<tab[j];
}

int bin2dec(int lb)
{ 
    int ldec = 0;
    int i = 1; 
    
    while (lb > 0) 
    {
        ldec += (lb%10)*i; 
        i = i*2; 
        lb /= 10;
    } 
    return ldec; 
} 

int main(int argc, char **argv)
{
    int ld = 0;
	cout << "Podaj dowolną liczbę dziesiętną: ";
    cin >> ld;
    
    int lb = 0;
	cout << "Podaj dowolną liczbę binarną: ";
    cin >> lb;
        
    cout << ld << " w systemie binarnym (dec2bin): " << dec2bin(ld) << endl;
    cout << ld << " w systemie binarnym (dectobin): ";
	dectobin(ld);
	cout << endl;
	cout << lb << " w systemie dziesiątkowym (bin2dec): " << dec2bin(lb) << endl; 
	return 0;
}
>>>>>>> ebdf89c047a3eece0a19b761bab6fed4fe688087
