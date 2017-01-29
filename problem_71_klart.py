#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock




if __name__ == '__main__':

	minval = 1000

	i = 4
	
	n = i
	d = 7*n/3 + 1
	
	while d <= 1000000:
		
		if 3.0/7 - (1.0*n)/d <= minval:
			minval = 3.0/7 - (1.0*n)/d
			minnums = (n,d)
			#print (n,d), minval
		
		i += 1
		
		n = i
		d = 7*n/3 + 1
	
	print minnums, minval