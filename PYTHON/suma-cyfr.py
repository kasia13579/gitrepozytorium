#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#  DANE WEJŚCIOWE: liczba "l2" co najmniej dwucyfrowa podawana przez użytkownika
#DANE WYJŚCIOWE: suma cyfr liczby l2 wydrukowana w terminalu

def suma_cyfr(l2):
    
    suma = 0
    
    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2 / 10)
        
    return suma

def main(args):
    
#    l2 = int(input("Podaj liczbę dwucyfrową: "))
#    
#    while l2 < 10:
#        l2 = int(input("Podaj liczbę dwucyfrową: "))
    
    assert(suma_cyfr(438) == 15)
    assert(suma_cyfr(1181) == 11)
    assert(suma_cyfr(26) == 8)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
