#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zlozonosc.py
#  
#  

def wersja1(args):
    n = int(input("LICZBA: "))
    for i in range(1, n, 2):
        print(i)
        
def wersja2(args):
    n = int(input("LICZBA: "))
    i = 1
    while i < n:
        print(1)
        1 += 2
        
        
def main(args):
    wersja2
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    
#  algorytm czesciowo poprawn, skonczony, zlozonosc liniowa (akgorytm liniowy, nie zawiera rozgalezien - instrukcji warunkowych)
