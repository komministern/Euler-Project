#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt


list_o_primes = [2, 3, 5, 7]
list_o_circular_primes = [2, 5]

def is_prime(n):
	prime = True
	i = 0
	while prime and list_o_primes[i] <= sqrt(n):
		if n % list_o_primes[i] == 0:
			prime = False
		i += 1
	return prime
	
def is_circular(n):
	set_o_digits = set( str(n) )
	circular = True
	if '2' in set_o_digits or '5' in set_o_digits or '0' in set_o_digits or '4' in set_o_digits or '6' in set_o_digits or '8' in set_o_digits:
		circular = False
	else:
		new_string = str(n) + str(n)
		for i in range(1, len(str(n)) ):
			if not is_prime( int( new_string[i:i+len(str(n))] ) ):
				circular = False
	return circular
			

if __name__ == '__main__':

	nbr = 11
	
	while nbr < 10 ** 6:
		if is_prime(nbr):
			list_o_primes.append(nbr)
		nbr += 2
		
	for p in list_o_primes:
		if is_circular(p):
			list_o_circular_primes.append(p)
	
	print len( list_o_circular_primes )
