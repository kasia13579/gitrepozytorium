/*
 * Dąda_lpierwsza.cpp
 * 
 * Copyright 2018  <>
 */


#include<iostream>

using namespace std;

bool lpierwsza(int n)
{
	if(n<2)
		return false;
	for(int i=2;i*i<=n;i++)
		if(n%i==0)
			return false;
	return true;
}

int main()
{
	int n;
	cout<<"Podaj liczbe: ";
	cin>>n;
	if(lpierwsza(n))
		cout<<"Liczba "<<n<<" jest pierwsza"<<endl;
	else
		cout<<"Liczba "<<n<<" jest zlozona"<<endl;
	return 0;
}
