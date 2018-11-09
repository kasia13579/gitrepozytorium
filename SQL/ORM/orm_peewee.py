#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
#  

import os
from peewee import * 

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik)

### MODEL DANYCH

class Klasa(Model):
    nazwa = CharField(null = False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
class Meta:
    database = baza
    
class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    

class Wynik(BazaModel):
    egz_hum = FloatField(default=0)
    egz_mat = FloatField(default=0)
    egz_jez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
