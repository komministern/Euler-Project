#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt, factorial
#from itertools import permutations
#from collections import OrderedDict


if __name__ == '__main__':

	
	#Brute force
	
	nbr = 0
	
	for n in range(20,101):
		
		for r in range(0,n+1):
			
			if factorial(n)/(factorial(r)*factorial(n-r)) > 10**6:
				nbr += 1
			
	print nbr