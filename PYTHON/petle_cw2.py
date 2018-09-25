#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw2.py
#  


def main(args):
    
    start = int(input("Podaj 1. liczbę: "))
    stop = int(input("Podaj 2. liczbę: "))
    
    if start < stop and start >= 0 and stop >= 0 :
        for liczba in range(start, stop + 1):
                print(liczba, " ", end="")
    else:
        print("błędny zakres")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

