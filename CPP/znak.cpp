/*
 * znak.cpp
 */


#include <iostream>

using namespace std;

void licz_znaki(char tab[]) {
    int i = 0;
    int biale, inter, licz;
    biale = inter = licz = 0;
        while(tab[i] != '\0') {
            cout << tab[i] << " ";
            //if (tab[i] == ' ' || tab[i] == '\t')
            //  biale++;
            // else
            //     cout << tab[i];
            switch(tab[i]) {
                    case ' ': biale++; break;
                    case '\t': biale++; break;
                    case ',': inter++; break;
                    case '.': inter++; break;
                    default: licz++; break;
                }
            i++;  // zwiększanie indeksu
        }
        cout << "\nZnaków białych: " << biale << endl;
        cout << "\nZnaków interpunkcyjnych: " << inter << endl;
    }

void ascii(char tab[]) {
    int i = 0;
    while(tab[i] != '\0') {
            cout << (int)tab[i] << " ";
            i++;
        }
    }
    
void zamiana_liter(char tab[]) {
    int i = 0;
    int kod;
    while(tab[i] != '\0') {
        kod = (int)tab[i];
        if (kod >= 65 && kod <=90)
            kod += 32;
        else if (kod >= 97 && kod <=122)
            kod -= 32;
        cout << (char)kod;
            i++;
        }
    }

int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char znaki[rozmiar];  // deklaracja tablicy znakowej
    cout << " Jak się nazywasz?";
    cin.getline(znaki, rozmiar);
    cout << " Cześć " << znaki << endl;
    ascii(znaki);
    zamiana_liter(znaki);	
	return 0;
}

