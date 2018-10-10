#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
#  

def silnia_it(n):
    # 0! = 1
    # 1! = 1
    # 4! = 24
    wynik = 1
    for i in range(1, n+1):
        print(wynik)
        wynik = i * wynik
    return wynik

def main(args):
    n = int(input("Podaj liczbę: "))
    print("{}! = {}".format(n, silnia_it(n)))
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
