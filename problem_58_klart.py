#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock

from math import sqrt

list_o_primes = [2, 3, 5, 7]

def isprime(n):
	prime = True
	i = 0
	while prime and list_o_primes[i] <= sqrt(n):
		if n % list_o_primes[i] == 0:
			prime = False
		i += 1
	return prime	



if __name__ == '__main__':


	nbr = 11
	
	while nbr < 10 ** 5:
		if isprime(nbr):
			list_o_primes.append(nbr)
		nbr += 2

	
	i = 0
	ndiagonals = 1.0
	nprimes = 0
	
	while nprimes / ndiagonals > 0.1 or nprimes == 0:
		i += 1
		
		for n in [(2*i+1)**2-2*i, (2*i+1)**2-4*i, (2*i+1)**2-6*i]:
			if isprime(n):
				nprimes += 1
				
		ndiagonals += 4
				
	print 2*i+1