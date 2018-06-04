#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = input("podaj ilość typowanych liczb: ")
    maksliczba = input("Podaj maksymalną losowaną liczbę")
    print("wytypuj () z () liczb") .format(ileliczb, maksliczba)

    # losowanie liczb
    liczby = []  3 lista wylosowanych liczb
    for i in range(ileliczb):
        if liczby.conut(liczba) = 0
        liczby.apppend
        liczba = random.randint(i, maksliczba +1)  # losowanie liczby <1;10>
    print("Podałeś:", odp)

       # if liczba == int(odp):  # porównanie odpowiedzi z wylosowaną liczbą
        #    print("Zgadłeś!")
         #   break  # przerwanie działania pętli
        #else:
         #   print("Spróbuj jeszcze raz!")

    return 3


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
