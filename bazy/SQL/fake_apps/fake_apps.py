#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []    # pusta lista
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]     # usuwa oceny
            dane.append(rekord)   # dodawanie rekordów do listy
    return dane


def main(args):
    con = sqlite3.connect('fake_apps.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('fake_apps.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie do bazy
    dane = dane_z_pliku('fake_apps.txt')
    dane.pop(0)
    cur.executemany('INSERT INTO fake_apps VALUES(?, ?, ?, ?, ?)', dane)

    con.commit()
    con.close()
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
