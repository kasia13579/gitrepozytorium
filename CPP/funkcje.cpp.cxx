/*
 * szkielet.cpp.cxx
 */


#include <iostream> //biblioteka wejścia wyjścia

using namespace std;

int suma(int a, int b)
{
    return a + b;
}

int roznica(int a, int b)
{
    return a - b;
}

int iloczyn(int a, int b)
{
    return a * b;
}

int iloraz(int a, int b)
{
    return a / b;
}


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
    cout << endl << "Suma: " << suma(a, b)<< endl;
    cout << endl << "Roznica: " << roznica(a, b)<< endl;
    cout << endl << "Iloczyn: " << iloczyn(a, b)<< endl;
    cout << endl << "Iloraz: " << iloraz(a , b)<< endl;
	
    //DRY - Don't repeat yourself.
    
	return 0;
}

