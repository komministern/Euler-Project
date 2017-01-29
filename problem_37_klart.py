#!/usr/bin/env python

#from numpy import *
from string import *
#from time import clock
from math import sqrt


def isPrime(n):
	if n < 2:
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

def isLeftTruncatable(n):
	
	ps = str(n)[1:]
		
	while len(ps) > 0:
			
		if not isPrime(int(ps)):
			return False
		else:
			ps = ps[1:]
	
	return True


if __name__ == '__main__':
	
	listofrighttruncprimes = []
	
	listofrighttruncprimestobetested = [2, 3, 5, 7]

	while len( listofrighttruncprimestobetested ) > 0:
	
		listofnewrighttruncprimes = []
	
		for p in listofrighttruncprimestobetested:
			
			for i in [1, 3, 7, 9]:
			
				if isPrime( p*10 + i ):
					listofnewrighttruncprimes.append( p*10 + i )
				
		listofrighttruncprimes = listofrighttruncprimes + listofnewrighttruncprimes 
			
		listofrighttruncprimestobetested = list( listofnewrighttruncprimes )
	
	listofrightlefttruncatableprimes = []
	
	for p in listofrighttruncprimes:
		if isLeftTruncatable(p):
			listofrightlefttruncatableprimes.append(p)
	
	print listofrightlefttruncatableprimes	
	
	print sum(listofrightlefttruncatableprimes)