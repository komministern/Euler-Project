#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt
#from itertools import permutations
from collections import OrderedDict

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
	while prime(i)**2 <= n:
		if n % prime(i) == 0:
			return False
		else:
			i += 1
	return True

def factors(n):
	lst = []
	nbr = n
	while not nbr == 1:
		i = 0
		while not nbr % prime(i) == 0:
			i += 1
		lst.append(prime(i))
		nbr = nbr / prime(i)
	return lst



if __name__ == '__main__':

	nprimefactors = []

	n = 4
	inarow = 0
	i = 1
	while inarow < n:
		i += 1
		if len(list(OrderedDict.fromkeys(factors(i)))) == n:
			inarow += 1
		else:
			inarow = 0
	
	print i-n+1
	
# FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUULT