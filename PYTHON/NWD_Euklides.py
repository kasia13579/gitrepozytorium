#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NWD_Euklides.py
#  


def nwd_klasyczny(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def main(args):
    a = int(input("Podaj 1. liczbę: "))
    b = int(input("Podaj 2. liczbę: "))
    print("Największy wspólny dzielnik {} i {} to {}" .format(a, b, nwd_klasyczny(a, b)))

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
