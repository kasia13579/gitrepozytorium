#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def pole(a, b):
    return a * b
    
def obwod(a, b):
    return 2 * a + 2 * b
    
def main(args):
    a = int(input("Podaj 1. liczbę: "))
    print(a)
    
    b = int(input("Podaj 2. liczbę: "))
    print(b)

    print("Pole: " , pole(a, b))
    print("Obwod: " , obwod(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
