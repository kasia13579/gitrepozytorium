/*
 * minmax.cpp
 */

#include <iostream>

using namespace std;

void wypelnij(int tab[], int roz){
    cout << "Podaj " << roz << " Liczb: " <<endl;
    for( int i = 0; i < roz; i++) {
        cin >> tab[i];
            }
}

void wypelnij_los(int tab[], int roz){
    srand(time(NULL));  // inicjacja generatora liczb pseudolosowych
    for( int i = 0; i < roz; i++) {
        tab[i] = rand()%101;
            }
}

void drukuj(int tab[], int roz){
    cout << "Podaj " << roz << " Liczb: " <<endl;
    for( int i = 0; i < roz; i++) {
        cout << tab[i] << " ";
            }
}

int main(int argc, char **argv)
{
	int rozmiar = 50;
    int tab[rozmiar];  // statyczna deklaracja tablicy
    wypelnij_los(tab, rozmiar);
    drukuj(tab, rozmiar);
	return 0;
}

