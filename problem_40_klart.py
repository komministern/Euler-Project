#!/usr/bin/env python

#from numpy import *
from string import *
#from time import clock
from math import sqrt



if __name__ == '__main__':
	
	s = ''
	i = 1
	while len(s) < 1000001:
		s = s + str(i)
		i = i +1
		
	print s[1-1]
	print s[10-1]
	print s[100-1]
	print s[1000-1]
	print s[10000-1]
	print s[100000-1]
	print s[1000000-1]

	print int(s[1000000-1])*int(s[100000-1])*int(s[10000-1])*int(s[1000-1])*int(s[100-1])*int(s[10-1])*int(s[1-1])
	