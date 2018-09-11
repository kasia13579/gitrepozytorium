/*
 * szkielet.cpp.cxx
 */


#include <iostream> //biblioteka wejścia wyjścia

using namespace std;

int main(int argc, char **argv) // int typl liczbowy; przechowuje liczby całkowite FUNKCJA GŁÓWNA
{
    int a, b; 
    a = b  = 0; 
    
    cout << "Podaj 1. liczbę: ";
    cin >> a;
    cout << a;
    
    cout << endl << "Podaj 2. liczbę: ";
    cin >> b;
    cout << b;
    cout << endl << "Suma: " << a + b << endl;
    cout << endl << "Iloraz: " << a / b << endl;
    cout << endl << "Różnica: " << a - b << endl;
    cout << endl << "Iloczyn: " << a * b << endl;
	
    //DRY - Don't repeat yourself.
    
	return 0;
}

