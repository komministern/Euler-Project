#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock



def ispalindrome(n):
	return str(n) == str(n)[::-1]

def iterate(n):
	return n + int(str(n)[::-1])

def test(n):
	nbr = n
	for i in range(50):
		nbr = iterate(nbr)
		if ispalindrome(nbr):
			return False
	return True

if __name__ == '__main__':

	nbroflychrel = 0
	i = 1
	
	while i <= 10**4:
		if test(i):
			nbroflychrel += 1
		i += 1
	
	print nbroflychrel
	
	
	
	
	