#!/usr/bin/env python

from numpy import *
from string import *
from time import clock

def min(y,x):
	if steps[y,x] != 0:
		return steps[y, x]
	else:
		if x == 80 - 1 and y == 80 - 1:
			steps[y, x] = matrix[y, x]
		elif x == 80 - 1:
			steps[y, x] = matrix[y, x] + min(y+1, x)
		elif y == 80 - 1:
			steps[y, x] = matrix[y, x] + min(y, x+1)
		else:
			down = min(y+1,x)
			right = min(y,x+1)
			if down < right:
				steps[y,x] = matrix[y,x] + down
			else:
				steps[y,x] = matrix[y,x] + right
		return steps[y, x]

if __name__ == '__main__':
	
	matrix = zeros([80,80])
	steps = zeros([80,80])

	f = open('./matrix.txt', 'r')

	y = 0
	str = f.readline()
	while str != '':
		matrix[y,:] = [int(each) for each in split(str, ',')]
		str = f.readline()
		y += 1
	f.close()
	
	print min(0,0)
	
