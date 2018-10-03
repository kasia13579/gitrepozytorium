#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat_rysunek.py
#  
#Dane wejściowe: boki a i b prostokata
#Dane wyjsciowe prostokat z gwiazdek o rozmiarach podanych przez uzytkownika

def prostokat(x,y):
    for i in range(10)
    for j in range(20)
    if j > 0 and j < y - 1:
        print(" ", end='')
        else:
            print("*",end='')
        else
            print("*", end='')
        print()
        

def main(args):
    
    a = int(input("Podaj długość a: "))
    b = int(input("Podaj długość b: "))
    znak = '*'
 
    for i in range(a):
        for j in range (b):
            print(znak, end='')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
