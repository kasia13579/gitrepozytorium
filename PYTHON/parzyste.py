#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py
#  



def main(args):
    
    start = int(input("Podaj 1. liczbę: "))
    stop = int(input("Podaj 2. liczbę: "))
    
    while start > stop:
        stop = int(input("Podaj większą liczbę niż pierwsza! Liczba 2: "))
        
    for liczba in range(start, stop + 1):
        # if liczba % 2 == 0:
        if not liczba % 2:
            print(liczba)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
