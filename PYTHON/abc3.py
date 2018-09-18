#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
#Program pobiera 3 liczby od użytkownika, a następnie wyświetla największą.
#

def maks(a, b, c):
    m = None
    if a > b:
        if a > c:
            m = a
    elif b > c:
        m = b
        print("Najwieksza:" , m)
        return m        

def main(args):
    assert(maks(3, 2, 1) ==3)
    assert(maks(3, 2, 1) ==3)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
