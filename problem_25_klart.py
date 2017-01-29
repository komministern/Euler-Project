#!/usr/bin/env python

from numpy import *
from string import *
from time import clock

if __name__ == '__main__':


	f_1 = 1
	f_2 = 1
	n = f_1 + f_2
	i = 3

	while len(str(n)) < 1000:
		f_2 = f_1
		f_1 = n
		n = f_1 + f_2
		i += 1
	
	print i