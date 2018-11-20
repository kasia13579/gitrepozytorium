#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwadrat.py
#  

import turtle


def rysujKwadrat(zolw, bok, ile):
    #  for i in range(4):
    zolw.forward(bok)
    zolw.right(90)
    if ile > 0:
        rysujKwadrat(zolw, bok, ile-1)


def rysujKwadrat2( zolw, bok):
    zolw.forward(bok)
    zolw.right(90)
    if bok > 10:
        rysujKwadrat(zolw, bok-10)
    


def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)
    
    zolw = turtle.Turtle()
    zolw.color('pink')
    
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
