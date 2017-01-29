#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt
from itertools import permutations
from collections import OrderedDict


def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


if __name__ == '__main__':

	primes = primes_sieve(1000000)
	
	longestseq = 1
	largestprime = 2
	seq = [2]
	
#	print primes
#	print sum(primes[0:1])
	
	k = 0

	while 10**6 - largestprime > seq[-1]:

		j = longestseq	

		while True:
			
			mysum = sum(primes[k:j])
		
			if mysum > primes[-1]:
				break
		
			if mysum in set(primes):
				if len(primes[k:j]) > longestseq:
					longestseq = len(primes[k:j])
					seq = primes[k:j]
					largestprime = mysum
				
					print mysum, len(primes[k:j])
			
			j += 1
		
		k += 1
		
		
	print seq, sum(seq)
	
	# Awful brute force.
	# Well, the correct result is given in a few secs. Lots of problems to go.
	# Onward and forward.