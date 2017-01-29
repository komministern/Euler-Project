#!/usr/bin/env python

from math import *


if __name__ == '__main__':

	sum = 0
	for digit in str(factorial(100)):
		sum += int(digit)
	
	print sum