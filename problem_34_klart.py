#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import factorial

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def sum_of_factorials(n):
	list = [factorials[ int(c) ] for c in str(n) ]
	sum = 0
	for each in list:
		sum += each
	return sum

if __name__ == '__main__':

	n = 1
	while n * factorials[9] > 10 ** n:
		n += 1
	
	#print n
	
	# Limit established
	
	list = []
	
	for nbr in range(3,10 ** n):
		
		if nbr == sum_of_factorials(nbr):
			list.append(nbr)
	
	sum = 0
	for each in list:
		sum += each
	
	print sum
	
	print list