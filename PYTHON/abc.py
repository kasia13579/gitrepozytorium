#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
#Program pobiera 3 liczby od użytkownika, a następnie wyświetla największą.
#

def main(args):
    a = int(input("Podaj 1. liczbę: "))
    print(a)
    
    b = int(input("Podaj 2. liczbę: "))
    print(b)
    
    if a > b:
        print(a, "jest większe od" , b)
        print(a, "jest różne od" , b)
    elif a < b:
        print(a, "jest mniejsze od" , b)
        print(a, "jest różne od" , b)    
    else:
        print(a, "jest równe" , b)        
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
