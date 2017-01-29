#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
from math import sqrt



def upper_right_diag(i):
	return i ** 2

def lower_left_diag(i):
	return (i - 2) ** 2 + i * 2 - 2

def lower_right_diag(i):
	return (i - 2) ** 2 + i - 1

def upper_left_diag(i):
	return i ** 2 - i + 1

if __name__ == '__main__':
	
	sum = 1
	for i in range(3, 1002, 2):
		sum += upper_right_diag(i) + lower_left_diag(i) + upper_left_diag(i) + lower_right_diag(i)
		
	print sum