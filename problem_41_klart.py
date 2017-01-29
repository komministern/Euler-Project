#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt
from itertools import permutations

def isprime(n):
	if n % 2 > 0:
		i = 3
		while i <= sqrt(n):
			if n % i == 0:
				return False
			i += 2 
		return True
	else:
		return False

if __name__ == '__main__':

	nbrstring = '123456789'
	primelist = []

	while len(primelist) == 0:
	
		l = list(map("".join, permutations(nbrstring)))
	
		for elem in l:
		
			if isprime(int(elem)):
				primelist.append(int(elem))
	
		nbrstring = nbrstring[:-1]
			
	print sorted(primelist)[-1]
	