#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock

from math import sqrt

primes = [2, 3, 5, 7]

def isprime(n):
	prime = True
	i = 0
	while prime and primes[i] <= sqrt(n):
		if n % primes[i] == 0:
			prime = False
		i += 1
	return prime	



if __name__ == '__main__':


	nbr = 11
	
	while nbr < 10 ** 6:
		if isprime(nbr):
			primes.append(nbr)
		nbr += 2

	lst = [[]]
	
	for i in range(10000):
		for j in range(10000):
			ps1 = str(primes[i])
			ps2 = str(primes[j])
			if isprime(int(ps1 + ps2)) and isprime(int(ps2 + ps1)):
				 lst[i].append(primes[j])				 
		lst.append([])
				 
	print set(lst[1]).intersection(set(lst[3])).intersection(set(lst[primes.index(109)]))
	
	
	
