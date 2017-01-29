#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock



def digitsum(n):
	return sum([int(d) for d in str(n)])

if __name__ == '__main__':


	largestsum = 0
	
	for a in range(100 + 1):
		for b in range(100 + 1):
			if digitsum(a**b) > largestsum:
				largestsum = digitsum(a**b)
				

	print largestsum
	
	
	
	