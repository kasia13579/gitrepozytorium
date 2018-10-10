#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby2-3.py
#

def main(args):

    print(liczby2(10, 99))
    print(liczby3(100, 999))

    return 0
    
def liczby2(a, b):
    """
    Drukuje wszystki liczby dwucyfrowe, którym nie powatarzają się cyfry
    11, 22, 33 ...
    Oraz zwraca ich ilość
    """

    c = 0

    for x in range(a, b + 1, 1):
        if x % 11 != 0:
            c = c + 1
            print(x)
    print("Liczba liczb: ", c)

    return ""


def suma_cyfr(a):
    suma = 0
    while a > 1:
        suma += a % 10
        a = int(a / 10)

    return suma


def liczby3(a, b):
    """
    Drukuje wszystkie liczby trzycyfrowe, nie powtarzają się cyfry
    Bez 111 112 233, 666
    """

    liczba = 0

    for x in range(a, b + 1, 1):
        c = x % 111
        d = x % 110
        e = x % 101
        g = x % 100
        if c != 0 and d != 0 and e != 0 and g != 0:
            z = 0
            z = int(x / 10)
            if z % 11 != 0:
                print(x)
            liczba = liczba + 1
    print("Liczba liczb: ", liczba)
    
    return ""


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
