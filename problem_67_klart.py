#!/usr/bin/env python

from numpy import *
from string import *
from time import clock

def max(y,x):
	if b[y,x] != 0:
		return b[y,x]
	else:
		if y == 99:
			return a[y,x]
		else:
			left = max(y+1,x)
			right = max(y+1,x+1)
			if left > right:
				b[y,x] = a[y,x] + left
				return b[y,x]
			else:
				b[y,x] = a[y,x] + right
				return b[y,x]

if __name__ == '__main__':

	a = zeros([100,100])
	b = zeros([100,100])

	f = open('./triangle.txt', 'r')

	y = 0
	str = f.readline()
	while str != '':
		x = 0
		for each in split(str):
			a[y,x] = int(each)
			x += 1
		str = f.readline()
		y += 1
	f.close()
	
	clock()
	
	print max(0,0)
	
	print clock()