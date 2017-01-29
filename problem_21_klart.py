#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt


def d(n):
	sum = 0
	for i in range(1, n / 2 + 1):
		if n % i == 0:
			sum += i
			#print sum
	return sum

if __name__ == '__main__':
	
	print d(220)
	print d(284)
	
	S = set([])
	
	a = 2
	while a <= 10000:
		b = d(a)
		if d(b) == a and a != b:
			print a, b
			S.add(a)
			#print 'Amicable found'
		a += 1
	
	sum = 0
	for each in S:
		sum += each
	
	print sum

	
	