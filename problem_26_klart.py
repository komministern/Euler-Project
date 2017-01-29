#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock

if __name__ == '__main__':

	longest_cycle = 6	
	d = 11
	while d < 1000:
		if d % 2 != 0 and d % 5 != 0:
			n = 1
			while n / d == 0:
				n *= 10
			
			first_remainder = n % d
			remainder = ((first_remainder * 10) % d)
			digit_cycle = 1
			
			while remainder != first_remainder:
				remainder = ((remainder * 10) % d)
				digit_cycle += 1
			
			if digit_cycle > longest_cycle:
				longest_cycle = digit_cycle
				denominator = d
				
		d += 1
			
	print denominator
	print longest_cycle 
			
	