#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   tabliczka_mnozenia.py 
#

def tabliczka(a, b):
    
    for i in range(1, a + 1):
        for j in rang(1, b + 1):
            print(i*j, end='')
        print()
