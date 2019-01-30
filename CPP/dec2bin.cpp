/*
 * dec2bin.cpp
 */


#include <iostream>
using namespace std;

void dec2bin(int l)
{
	int i=0,tab[255];
	while(l){   
        tab[i++]=l%2;
		l/=2;
	}
	for(int j=i-1;j>=0;j--)
		cout<<tab[j];
}

int main()
{
	int l;
	cout<<"Podaj liczbę: ";
	cin>>l;
	dec2bin(l);
	cout<<endl;
    
	return 0;
}

