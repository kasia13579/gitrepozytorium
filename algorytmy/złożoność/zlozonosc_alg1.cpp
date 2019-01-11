/*
 * zlozonosc_alg1.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
 int a = 0;
    cout << "Podaj a: ";
    cin >> a;
    if (a <= 0 or a > 99) {
        cout << "Podaj a: ";
        cin >> a;
        }
    for (int i = 2; i < 100; i += 2) {
        if (a == i) {
            cout << "a parzyste";
            }
        if (i == 100) {
            cout << "a nieparzyste";
        }
    }

    return a;
}

