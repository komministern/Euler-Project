#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt


def p200():
	n = 0
	i = 0
	while i * 200 <= 200:
		n += p100(i * 200)
		i += 1
	return n

def p100(sum):
	n = 0
	i = 0
	while sum + i * 100 <= 200:
		n += p50(sum + i * 100)
		i += 1
	return n

def p50(sum):
	n = 0
	i = 0
	while sum + i * 50 <= 200:
		n += p20(sum + i * 50)
		i += 1
	return n
		
def p20(sum):
	n = 0
	i = 0
	while sum + i * 20 <= 200:
		n += p10(sum + i * 20)
		i += 1
	return n
	
def p10(sum):
	n = 0
	i = 0
	while sum + i * 10 <= 200:
		n += p5(sum + i * 10)
		i += 1
	return n
	
def p5(sum):
	n = 0
	i = 0
	while sum + i * 5 <= 200:
		n += p2(sum + i * 5)
		i += 1
	return n
	
def p2(sum):
	n = 0
	i = 0
	while sum + i * 2 <= 200:
		n += p1(sum + i * 2)
		i += 1
	return n	
	
def p1(sum):
	return 1


if __name__ == '__main__':
	
	print p200()
