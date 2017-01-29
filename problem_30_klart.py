#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt




if __name__ == '__main__':
	
	list = []
	
	
	for n in range(3,6 * 9**5):
	
		string = str(n)
		sum = 0
		i = 0
		while i != len(string):
			sum += int( string[i] ) ** 5
			i += 1
		
		if sum == n:
			list.append(n)
		
	print list
	
	sum = 0
	for each in list:
		sum += each
	
	print sum