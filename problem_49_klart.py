#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt
from itertools import permutations
from collections import OrderedDict


if __name__ == '__main__':

	list_of_primes = [2, 3, 5]
	
	nbr = 7
	
	while list_of_primes[-1] < 10000:
		
		i = 0
		prime = True
		while list_of_primes[i] <= int( sqrt( nbr ) ):
			if nbr % list_of_primes[i] == 0:
				prime = False
				break
			else:
				i += 1
		if prime:
			list_of_primes.append( nbr )
			
		nbr += 2
	
#	print list_of_primes

	list_of_four_digit_primes = [n for n in list_of_primes if len(str(n)) == 4]
	
#	print list_of_four_digit_primes
	
	
	for p in list_of_four_digit_primes:
		
		aset = set(list_of_four_digit_primes).intersection(set([int(''.join(s)) for s in permutations(str(p))]))
#		print p, len(set(list_of_four_digit_primes).intersection(set([int(''.join(s)) for s in permutations(str(p))])))
		
		while len(aset) >= 3:
			
			i = 1
			while i < len(aset) - 1:
		
				if sorted(aset)[0] + 1 * (sorted(aset)[i] - sorted(aset)[0]) in aset and sorted(aset)[0] + 2 * (sorted(aset)[i] - sorted(aset)[0]) in aset:
			
					print [sorted(aset)[0], sorted(aset)[0] + 1 * (sorted(aset)[i] - sorted(aset)[0]), sorted(aset)[0] + 2 * (sorted(aset)[i] - sorted(aset)[0])]
					list_of_four_digit_primes = list(set(list_of_four_digit_primes).difference(aset))
				
				i += 1
		
			aset = set(sorted(aset)[1:])
		
	#aset = set(list_of_four_digit_primes).intersection(set([int(''.join(s)) for s in permutations(str(1487))]))
	#print aset
	#print sorted(aset)
