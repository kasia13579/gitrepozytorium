/*
 * szkielet.cpp.cxx
 */


#include <iostream> //biblioteka wejścia wyjścia

using namespace std;

int main(int argc, char **argv) // int typl liczbowy; przechowuje liczby całkowite FUNKCJA GŁÓWNA
{
    int liczba; // deklaracja zmiennej liczby typu całkowitego
    liczba = 12.78;
   // std::cout << liczba;

    int a, b, c, d; // deklaracja
    a = b = c = d = 0; //inicjalizacja zmiennych
    a = 10;
    b = 2 * a;
    c = b-a;
    d = a/b; 
    
    cout << "\n" << a << " " << b << " " << c;
	
	return 0;
}

