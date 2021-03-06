#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maks. losowaną liczbę: "))
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))

    # losowanie liczb

    liczby = []   # lista wylosowanych liczb
    i = 0
    # for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba)  # losowanie liczby <1;10>
        if liczby.count(liczba) == 0:  # sprawdzenie czy wartość jest w liście
            liczby.append(liczba)
            i += 1  # powiększ i o 1
    print(liczby)

    typy = set()  # deklaracja pustego zbioru na typyuzytkownika
    i = 0
    while i < ileliczb:
        typ = input("Podaj liczbę", i + 1)
        if typ not in typy:  # jeżeli podanego typu nie ma w zbiorze
            typy.add(typ)
            i += 1

        # odp = input("Podaj liczbę od 1 do 10: ")
        # print("Podałeś:", odp)

        # if liczba == int(odp):  # porównanie odpowiedzi z wylosowaną liczbą
        #     print("Zgadłeś!")
        #     break  # przerwanie działania pętli
        # else:
        #     print("Spróbuj jeszcze raz!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
