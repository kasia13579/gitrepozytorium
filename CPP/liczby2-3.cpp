/*
 * liczby2-3.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;


int liczby2() {
    int ile = 0; // deklaracja + inicjacja = definicja
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++){
             if (i != j){
            cout << i << j << " ";
            ile++;
            }
        }
    }
    return ile;
}

int liczby3() {
    int ile2 = 0; // deklaracja + inicjacja = definicja
    for (int k = 1; k < 10; k++) {
        for (int l = 0; l < 10; l++){
            for (int m = 0; m < 10; m++){
                if (k != l && m ! = l  && k ! = m){
                cout << k << l << m << " ";
                ile2++;
                }
            }
        }
    }
    return ile2;
}

int main(int argc, char **argv){

    int ile = liczby2();
    cout << "\n\nLiczby 2-cyfrowe: " << ile <<endl;
	return 0;
    
    int ile2 = liczby3();
    cout << "\n\nLiczby 3-cyfrowe: " << ile2 <<endl;
	return 0;
}

