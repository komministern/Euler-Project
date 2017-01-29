#!/usr/bin/env python

#from numpy import *
from string import *
#from time import clock
#from math import sqrt


def pandigital(s):
	if len(''.join(set(s))) == len(s) and set(s) == set('123456789'):
		return True
	else:
		return False
	
	
if __name__ == '__main__':
	
	listonumbers = []
	
	for n in range(50000):
		
		s = ''
		i = 1
		while len(s) < 9:
			s += str(n*i)
			i += 1
		if len(s) == 9:
			if pandigital(s):
				listonumbers.append(int(s))
		
	print sorted(listonumbers)[-1]