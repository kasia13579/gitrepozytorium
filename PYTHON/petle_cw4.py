#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw4.py
#  



def main(args):
	
	for i in range(10, 100):
		if i %3 ==0 and i %2 == 0:
			print (i)

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
