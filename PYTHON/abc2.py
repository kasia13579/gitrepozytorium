#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
#Program pobiera 3 liczby od użytkownika, a następnie wyświetla największą.
#

def maks(a, b, c):
    m= None
    if a > b:
        if a > c:
            m = a
    elif b > c:
        m = b
        print("Najwieksza:" , m)
        return m        

def main(args):
    a = int(input("Podaj 1. liczbę: "))
    print(a)
    
    b = int(input("Podaj 2. liczbę: "))
    print(b)
    
    c = int(input("Podaj 3. liczbę: "))
    print(c)
    
    if a > b and a > c:
        print(a, "jest największe")
    elif b > a and b > c:
        print(b, "jest największe")  
    if c > b and c > a:
        print(c, "jest największe")       
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
