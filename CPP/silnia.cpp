/*
 * silnia.cpp
 */

#include <iostream>
using namespace std;

int silnia_re(int n) {
    if (n == 0) return 1;
    else return n*silnia_re(n-1);

}

int main(int argc, char **argv){
    int n;
    cout << "Podaj liczbę: "; cin >> n;
    cout <<"Wynik: " << silnia_re(n) << endl;
    return 0; 
    
}
    
