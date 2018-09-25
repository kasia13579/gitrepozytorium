#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
#Program pobiera 3 liczby od użytkownika, a następnie wyświetla największą.
#

def maks(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


def main(args):
    assert(maks(3, 2, 1) == 3)
    assert(maks(3, 1, 2) == 3)
    assert(maks(3, 1, 3) == 3)
    assert(maks(3, 2, 3) == 3)
    assert(maks(3, 2, 2) == 3)
    assert(maks(3, 1, 1) == 3)
    assert(maks(3, 3, 1) == 3)
    assert(maks(3, 3, 2) == 3)
    assert(maks(3, 3, 3) == 3)
    assert(maks(2, 1, 3) == 3)
    assert(maks(2, 3, 1) == 3)
    assert(maks(2, 3, 2) == 3)
    assert(maks(2, 2, 3) == 3)
    assert(maks(2, 3, 3) == 3)
    assert(maks(1, 2, 3) == 3)
    assert(maks(1, 3, 2) == 3)
    assert(maks(1, 3, 3) == 3)
    assert(maks(1, 1, 3) == 3)
    assert(maks(1, 3, 1) == 3)
	
    
    return 0 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
