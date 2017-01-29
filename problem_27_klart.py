#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt

def quad(n, a, b):
	return n ** 2 + a * n + b

def isPrime(n):
	if n < 0:
		return False
	else:
		i = 2
		prime = True
		while i <= sqrt(n) and prime == True:
			if n % i == 0:
				prime = False
			else:
				if i == 2:
					i += 1
				else:
					i += 2
		return prime


if __name__ == '__main__':

	max_consecutive_primes = 0

	for a in range(-1000, 1001):
		#print a
		for b in range(-1000, 1001):
			#print b
			
			n = 0
			while isPrime( quad(n, a, b) ):
				n += 1
			
			if n > max_consecutive_primes:
				max_consecutive_primes = n
				a_max = a
				b_max = b
				
	print max_consecutive_primes
	print 'a =', a_max
	print 'b =', b_max
	print 'Product: a * b =', a_max * b_max