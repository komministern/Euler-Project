#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import factorial
from itertools import permutations



if __name__ == '__main__':
	
	l = list(map("".join, permutations('123456789')))
	nl = []
	
	for elem in l:
		if (int(elem[:2]) * int(elem[2:5]) == int(elem[5:])) or (int(elem[:1]) * int(elem[1:5]) == int(elem[5:])):
			nl.append(int(elem[5:]))
			
	
	uniquelist = []
	
	[uniquelist.append(item) for item in nl if item not in uniquelist]
	
	print uniquelist
	
	print sum(uniquelist)