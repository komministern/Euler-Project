#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock


def sumofdivisors(n):
    return sum([i for i in range(1, n / 2 + 1) if n % i == 0])

        
        
   

if __name__ == '__main__':
	
	n = 1000000
	divsum = [1] * (n + 1)

	for i in range(2, n/2 + 1):
		j = i*2 
		while j <= n:
			divsum[j] += i
			j += i


	tested = [False] * (n + 1)

	
	chains = []
	for each in divsum:
		
		if each <= n:
			i = each
			chain = []
			while i not in chain and not tested[i]:
				tested[i] = True
				chain.append(i)
				i = divsum[i]
				if i > n:
					break
			if i in chain:
				chains.append(chain[chain.index(i):])
		
		
					
	l = 0
	c = []
	for each in chains:
		if len(each) >= l:
			l = len(each)
			c = each
			
	print c
	print sorted(c)
	#print chains