#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy_orm.py
#  
from modele import *

def main(args):
    baza.connect()
    
    kw01()
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
