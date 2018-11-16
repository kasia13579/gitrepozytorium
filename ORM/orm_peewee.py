#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy


### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')

def main(args):
    if os.path_exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl2a = Klasa(nazwa="2A", roknaboru=2010, rokmatury=2013)
    kl2a.save()
    
    ul = Uczen(imie="Jarosław" nazwisko="Mały", plec=False, klasa=kl2a)
    ul.save()
    
    kl1a = Klasa(nazwa="1A", roknaboru=2009, rokmatury=2012)
    kl2a.save()
    
    ul = Uczen(imie="Anna" nazwisko="Gacek", plec=True, klasa=kl1a)
    ul.save()
    
    ul = Uczen(imie="Roman" nazwisko="Polek", plec=False, klasa=kl1a)
    ul.save()
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.nazwisko, uczen.klasa.nazwa)
        
    return 0

# dodaj klasę 1A, 2009, 2012
# dodaj uczniow do klasy 1A: Anna Gacek, Roman Polek

    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
