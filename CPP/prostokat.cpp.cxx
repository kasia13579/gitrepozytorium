/*
 * prostokat.cpp.cxx
 */


#include <iostream>


using namespace std;

int pole(int a, int b)
{
    return a * b;
}

int obwod(int a, int b)
{
    return 2 * a + 2 * b;
}

int main(int argc, char **argv)
{
    int a, b; 
    a = b  = 0; 
    
    cout << "Podaj 1. liczbę: ";
    cin >> a;
    cout << a;
    
    cout << endl << "Podaj 2. liczbę: ";
    cin >> b;
    cout << b;
    cout << endl << "Pole: " << pole(a, b)<< endl;
    cout << endl << "Obwod: " << obwod(a, b)<< endl;
	
	return 0;
}

