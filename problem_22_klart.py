#!/usr/bin/env python

from numpy import *
from string import *
from time import clock

def value(name):
	sum = 0
	for letter in name:
		sum += ord(letter) - ord('A') + 1
	return sum

if __name__ == '__main__':


	f = open('./names.txt', 'r')
	str = f.readline()
	f.close()
	
	#print str
	
	str = str.replace(',', ' ')
	str = str.replace('"', '')
	list = str.split()
	list.sort()
	
	sum = 0
	i = 1
	for name in list:
		sum += i * value(name)
		i += 1
	
	print sum
	
	