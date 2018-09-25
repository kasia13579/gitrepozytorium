#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#  



def trojkat(a,b,c):
    """ 
    Funkcja przyjmuje trzy liczby - dlugosci cokow trojkata.
    Funkcja sprawdza, czy da sie z nich zbudować trojkat.
    Funkcja zwraca True jeśli się da, False w przeciwnym razie.
    """
    wynik = False
    
    # warunek1 and warunek2
    # warunek1 or warunek2
    # not warunek1 
    
    if a + b > c and a + c > b and b + c > a:
        wynik = True # da się zbudować trójkąt
    return wynik
    
    
def main(args):
    assert(trojkat(3, 6, 8) == True)
    assert(trojkat(3, 5, 9) == False)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
