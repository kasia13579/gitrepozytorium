#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste2.py
#  



def main(args):
    
    start = int(input("Podaj 1. liczbę: "))
    stop = int(input("Podaj 2. liczbę: "))
    
    if start < stop:
        for liczba in range(start, stop + 1):
            # if liczba % 2 == 0:
            if not liczba % 2:
                print(liczba)
    else:
        print("błędny zakres")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
