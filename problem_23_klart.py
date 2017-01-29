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
	
	#print d(28)
	
	S = set([])
	
	for each in range(1, 28123 + 1):
		if each < d(each):
			S.add(each)
			#print each

	#print S

	print 'Abundant set ready'
	#print len(S)

	sum = 0
	for n in range(1, 28123 + 1):
		sum_of_abundant = False
		for i in range(12, n + 1):
			if i in S and n - i in S:
				sum_of_abundant = True
				break
		if not sum_of_abundant:
			sum += n
		
	print sum