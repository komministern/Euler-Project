#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt, factorial
#from itertools import permutations
#from collections import OrderedDict




def testn(n):
	if len(set(str(n)).symmetric_difference(set(str(2*n)))) == 0:
		if len(set(str(n)).symmetric_difference(set(str(3*n)))) == 0:
			if len(set(str(n)).symmetric_difference(set(str(4*n)))) == 0:
				if len(set(str(n)).symmetric_difference(set(str(5*n)))) == 0:
					if len(set(str(n)).symmetric_difference(set(str(6*n)))) == 0:
						return True
	return False


if __name__ == '__main__':

	
	#Brute force
	
	n = 1
	
	while True:
		
		if testn(int('1'+str(n))):
			break
		else:
			n += 1
			
	print '1' + str(n)