#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock


def next((a,b)):
	return (2*b + a, a + b)


if __name__ == '__main__':

	(a,b) = (1,1)
	n = 0
	i = 1
	
	while i <= 1000:
		(a,b) = next((a,b))
		if len(str(a)) > len(str(b)):
			n += 1
		i += 1
	
	
	
	print n
	
	