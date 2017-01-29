#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt
#from itertools import permutations


listofprimes = [2, 3, 5]

def prime(i):
	if len(listofprimes) > i:
		return listofprimes[i]
	else:
		p = listofprimes[-1] + 2
		while not isprime(p):
			p += 2
		listofprimes.append(p)
		return prime(i)

def isprime(n):
	i = 0
	while prime(i) <= sqrt(n):
		if n % prime(i) == 0:
			return False
		else:
			i += 1
	return True

def conjectureholds(n):
	i = 1
	while 2*i**2 < n-1:
		if isprime(n - 2*i**2):
			return True
		else:
			i += 1
	return False

if __name__ == '__main__':

	i = 9
	while conjectureholds(i):
		i += 2
		while isprime(i):
			i += 2
	
	print i
	