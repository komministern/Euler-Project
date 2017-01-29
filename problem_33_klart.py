#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import fabs

def is_digit_in_number(d, n):
	return str(d) in set( str(n) )

def remove_digit_from_number(d, n):
	string_n = str(n)
	if string_n[0] == str(d):
		return int( string_n[1] )
	else:
		return int( string_n[0] )

if __name__ == '__main__':

	list = []

	for num in range(10, 51):
	
		for denum in range(10, 100):
		
			for d in range(1, 10):
				
				if is_digit_in_number(d, num) and is_digit_in_number(d, denum):
					
					new_num = 1.0*remove_digit_from_number(d, num)
					new_denum = 1.0*remove_digit_from_number(d, denum)
					
					#print new_num
					#print new_denum
					
					if new_denum != 0 and new_num != 0 and new_denum != new_num:
						#print fabs(((1.0*new_num) / 1.0*new_denum - (1.0*num) / 1.0*denum))
						if fabs(new_num/new_denum - 1.0*num/denum) < 0.0001:
							list.append( (num, denum) )
					
	print list
	