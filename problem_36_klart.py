#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt


def isPalindrome(s):

	while len(s) > 1:
		if s[0] != s[-1]:
			return False
		else:
			s = s[1:-1]
	return True

if __name__ == '__main__':

	s = 0
	i = 1
	
	while i < 999999:
		if isPalindrome(str(i)):
			if isPalindrome(bin(i)[2:]):
				print i
				s = s + i
		i = i + 1
		
	print s
	
