#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py
#  DANE WEJŚCIOWE: liczba "l2" co najmniej dwucyfrowa podawana przez użytkownika
#DANE WYJŚCIOWE: suma cyfr liczby l2 wydrukowana w terminalu

def sumuj_cyfry(l2):
    suma = 0
    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2 / 10)
    return suma

def main(args):

    #l2 = int(input("Podaj liczbę 2-cyfrową: "))
    #while l2 < 10:
    #    l2 = int(input("Podaj liczbę 2-cyfrową: "))
    
    assert(sumuj_cyfry(111) ==3)
    assert(sumuj_cyfry(256) ==13)
    assert(sumuj_cyfry(12341) ==11)
    assert(sumuj_cyfry(1245) ==12)
    
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
