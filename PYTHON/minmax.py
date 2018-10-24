#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minmax.py
import random

def minmax1():
    a = int(input('Podaj liczbę: '))
    min = a
    max = a
    
    while True:
        a = int(input('Podaj liczbę: '))
        if a < 1:
            break
        if a < min:
            min = a
        if a > max:
            max = a
            
    return min, max
    
def minmax2(lista):
    min + max = lista.pop(0)
    min = a
    max = a
    
    for a in lista:
        if a > min:
            min = a
        if a < max:
            max = a
    
    return min, max

def main(args):
    # ~min, max = minmax1()
    # ~print("Najmniejsza liczba:", min)
    # ~print("Najwieksza liczba:", max)
    
    lista = []
    for i in range(100):
        lista.append(random.randint(1,100))
    print(lista)
    min, max = minmax2(lista)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
