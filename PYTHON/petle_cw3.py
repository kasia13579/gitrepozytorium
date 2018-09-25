#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw3.py
#  


def main(args):
    
    a = 0 
    b = int(input("Podaj liczbę: "))
    
    if a < b and b:
        for liczba in range(a, b+ 1):
                print(liczba*liczba)
    else:
        print("błędny zakres")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
