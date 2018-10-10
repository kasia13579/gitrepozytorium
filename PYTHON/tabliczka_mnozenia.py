#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka_mnozenia.py
#


def main(args):

    a = int(input("Podaj pierwszą liczbę zakresu mnożenia: "))
    b = int(input(" Podaj ostatnią liczbę zakresu mnożenia: "))

    for i in range(1, a + 1, 1):  # pętla zewnętrzna
        for j in range(1, b + 1, 1):
            print("{:>4}" .format(i * j), end='')
        print()  # znak końca linii

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
