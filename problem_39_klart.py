#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt


def f(p,a,b):
	return p**2 - 2*p*(a+b) + 2*a*b

	
if __name__ == '__main__':

	max_solutions = 0
	perimeter = 0
	
	for p in range(5,1000):

		l = []
#		p = 120
	
		for i in range(1,p/2):
			for j in range(i+1,p/2):
				if f(p,i,j) == 0:
					l.append(list([i,j,p]))
				
		if len(l) > max_solutions:
			max_solutions = len(l)
			perimeter = p
	
	
	print max_solutions
	print perimeter
	
#	En allt for brutal losning. Inte snyggt.