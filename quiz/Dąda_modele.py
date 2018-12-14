#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#  

import os  
from peewee import *
baza_plik = 'modele.db'
baza = SqliteDatabase(baza_plik) 


class BazaModel(Model):
    class Meta:
        database = baza


class Kategoria(BazaModel):
    kategoria = CharField()


class Pytanie(BazaModel):
   pytanie = CharField()
   id_kat = ForeignKeyField(Kategoria, related_name='kategoria')
   
    
class Odpowiedz(BazaModel):
    id_p = ForeignKeyField(Pytania, related_name='pytania')
    odpowiedz = CharField()
    odpok = BooleanField()


def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect()
    baza.create_tables([Kategoria, Pytanie, Odpowiedz])
        
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
