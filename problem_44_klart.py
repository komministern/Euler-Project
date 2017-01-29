#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt
#from itertools import permutations

def P(i):
	return i*(3*i-1)/2

def ispentagonal(n):
	if (sqrt(24*n+1)+1)/6 % 1 == 0:
		return True
	else:
		return False

		

if __name__ == '__main__':

	i = 2
	j = 1
	
	nbrs = []
	
	while (len(nbrs) == 0) or (P(i)-P(i-1) < nbrs[0]):
		#print P(i)-P(i-1)
		j = 1
		while i > j:
			if ispentagonal(P(i)-P(j)):
				if ispentagonal(P(i)+P(j)):
					print P(i)-P(j)
					nbrs.append(P(i)-P(j))
				j += 1
			else:
				j += 1
		i += 1
	print 'Klart.'
		
# This algorithm shows that the number weve come up with actually is the smallest
# possible. But it takes hours or weeks. Hmmm. More thinking power needed. When can we
# be sure that no smaller number is possible? 