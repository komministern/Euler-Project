#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt
#from itertools import permutations

def T(i):
	return i*(i+1)/2

def P(i):
	return i*(3*i-1)/2

def H(i):
	return i*(2*i-1)

def ispentagonal(n):
	if (sqrt(24*n+1)+1)/6 % 1 == 0:
		return True
	else:
		return False

def istriangular(n):
	if (sqrt(8*n+1)-1)/2 % 1 == 0:
		return True
	else:
		return False

if __name__ == '__main__':

	i = 144
	
	while not (istriangular(H(i)) and ispentagonal(H(i))):
		i += 1
		
	print H(i)
	