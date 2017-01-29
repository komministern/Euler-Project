#!/usr/bin/env python

#from numpy import *
from string import *
#from time import clock


def tnr(n):
	return n*(n+1)/2

def letterposition(s):
	return uppercase.index(s) + 1

def isTriangular(n):
	i = 1
	while tnr(i) < n:
		i = i + 1
	if n == tnr(i):
		return True
	else:
		return False
		

if __name__ == '__main__':
	
	words = []
	
	f = open('./words.txt', 'r')

	words = f.read().translate(None, '"').split(',')
	
	f.close()
		
	nbroftwords = 0
	
	for s in words:
		
		n = 0
		for c in s:
			n = n + letterposition(c)
	
		if isTriangular(n):
			nbroftwords = nbroftwords + 1
			print s
			
	print nbroftwords