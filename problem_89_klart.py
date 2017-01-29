#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock


pairlst = [(1000,'M'), (500,'D'), (100,'C'), (50,'L'), (10,'X'), (5,'V'), (1,'I')]

order = 'IVXLCDM'

dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def decimal(s):
	
	#print s
	
	n = 0
	while len(s) >= 2:
		if dict[s[-2]] < dict[s[-1]]:
			n += dict[s[-1]] - dict[s[-2]]
			s = s[:-2]
		else:
			n += dict[s[-1]]
			s = s[:-1]
	
	if len(s) > 0:
		n += dict[s[-1]]
	return n

	
def roman(n):
	s = ''
	for pair in pairlst:
		m = n / pair[0]
		n -= m * pair[0]
		s += pair[1] * m
	return s


def shortest(s):

	ns = ''
	
	while len(s) > 0:
	
		if len(s) >= 4:
	
			# Only I, X, C, or M (!) can occur in multiples of four.
	
			if len(set(s[-4:])) == 1:
				
				if len(s) > 4:
	
					if order.index(s[-5]) - order.index(s[-4]) == 1:
				
						ns += order[order.index(s[-1]) + 2]
						ns += s[-1]
						s = s[:-5]
						
					else:
					
						ns += order[order.index(s[-1]) + 1]
						ns += s[-1]
						s = s[:-4]
						
				else:
					
					if len(set(s)) == 1 and not s[-1] == 'M':
					
						ns += order[order.index(s[-1]) + 1]
						ns += s[-1]
						s = ''
						
					else:
						ns += s[-1]
						s = s[:-1]
					
			else:
						
				ns += s[-1]
				s = s[:-1]
		else:
			ns += s[-1]
			s = s[:-1]
			
	return ns[::-1]


if __name__ == '__main__':

	f = open('./p089_roman.txt', 'r')

	numerals = f.readlines()
	
	f.close()
	
	n = 0
	
	numerals = [each.replace('\n', '') for each in numerals]
	
	for each in numerals:
		
		#k = len(each) - len(shortest(roman(decimal(each))))
	
		n += len(each) - len(shortest(roman(decimal(each))))
	
	print n
	

	
	
	