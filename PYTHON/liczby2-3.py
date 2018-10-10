#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby2-3.py
#

def liczby2(a, b):
    """
    Drukuje wszystki liczby dwucydrowe, którym nie powatarzają się cyfry
    np.: 11, 22, 33 ...
    Oraz zwraca ich ilość
    """

    d = 0

    for x in range(a, b + 1, 1):
        if x % 11 != 0:
            d = d + 1
            print(x)
    print("Ilośc takich liczb: ", d)

    return ""


def suma_cyfr(x):
    suma = 0
    while x > 1:
        suma += x % 10
        x = int(x / 10)

    return suma


def liczby3(a, b):
    """
    Drukuje wszystkie liczby 3 cyfrowe, gdzie nie powtarzają się cyfry
    Bez 111 112 11x, 66x itd
    """

    ilosc = 0

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
            ilosc = ilosc + 1
    print("Ilośc takich liczb: ", ilosc)

    return "To była funkcja Liczby3"


def main(args):

    print(liczby2(10, 99))
    print(liczby3(100, 999))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
