/*
 * anagram.cpp
 */

// anagram() - funkcja odwraca znaki w pojedynczym wyrazie
// wyrazy() - funkcja dzieli tekst na wyrazy, znaleziony wyraz przekazuje do funkcji anagram

#include <iostream>

using namespace std;

int zlicz(char tb[]){
        int i = 0;
        while(tb[i] != '\0') i++;
        return i;
    }

void wyswietl(char tekst[], int roz) {
        for(int i=k-1;i>=0;i--){
                cout << tekst[i];
            }
    }


int main(int argc, char **argv)
{
    const int roz = 50;
	char tekst[roz];
    cin.getline(tekst, roz);
    wyswietl(tekst, zlicz(tekst));
	return 0;
}

