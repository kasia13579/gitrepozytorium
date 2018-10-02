#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#  DANE WEJŚCIOWE: liczba "l2" co najmniej dwucyfrowa podawana przez użytkownika
#DANE WYJŚCIOWE: suma cyfr liczby l2 wydrukowana w terminalu

def suma_cyfr(l2):
    
    suma = 0
    
    for cyfra in l2:
		suma += cyfra
		        
    return suma

def main(args):
    
#    l2 = int(input("Podaj liczbę dwucyfrową: "))
#    
#    while l2 < 10:
#        l2 = int(input("Podaj liczbę dwucyfrową: "))
    
	assert(suma_cyfr("113571975") == 39)
	assert(suma_cyfr("9234566542") == 46)
	assert(suma_cyfr("12765400002") == 27)
    
	return 0

if __name__ == '__main__':
    import sys
	sys.exit(main(sys.argv))

