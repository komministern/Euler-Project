#!/usr/bin/env python

from numpy import *
from string import *
from time import clock
import sys

#sys.setrecursionlimit(1500)

def min(y,x,latest_direction):
	if steps[y, x] == 0:
		if x == 80 - 1:
			steps[y, x] = matrix[y, x]
		else:
			if y == 0:
				right = min(y, x+1, 'r')
				if latest_direction != 'u':
					down = min(y+1, x, 'd')
				if latest_direction == 'u':
					steps[y, x] = matrix[y, x] + right
				elif down <= right:
					steps[y, x] = matrix[y, x] + down
				else:
					steps[y, x] = matrix[y, x] + right
			elif y == 80 - 1:
				right = min(y, x+1, 'r')
				if latest_direction != 'd':
					up = min(y-1, x, 'u')
				if latest_direction == 'd':
					steps[y, x] = matrix[y, x] + right
				elif up <= right:
					steps[y, x] = matrix[y, x] + up
				else:
					steps[y, x] = matrix[y, x] + right
			elif y <= 79 and y >= 0:
				right = min(y, x+1, 'r')
				if latest_direction != 'u':
					down = min(y+1, x, 'd')
				if latest_direction != 'd':
					up = min(y-1, x, 'u')
				
				if latest_direction == 'u':
					if up <= right:
						steps[y, x] = matrix[y, x] + up
					else:
						steps[y, x] = matrix[y, x] + right
				elif latest_direction == 'd':
					if down <= right:
						steps[y, x] = matrix[y, x] + down
					else:
						steps[y, x] = matrix[y, x] + right
				elif latest_direction == 'r':
					if up <= right and up <= down:
						steps[y, x] = matrix[y, x] + up
					elif down <= right and down <= up:
						steps[y, x] = matrix[y, x] + down
					else:
						steps[y, x] = matrix[y, x] + right
	return steps[y, x]
					
					
	

if __name__ == '__main__':
	
	matrix = zeros([80,80])
	#steps = zeros([80,80])

	f = open('./matrix.txt', 'r')

	y = 0
	str = f.readline()
	while str != '':
		matrix[y,:] = [int(each) for each in split(str, ',')]
		str = f.readline()
		y += 1
	f.close()
	
	list = []
	
	for i in range(80):
		steps = zeros([80,80])
		list.append(min(i,0,'r'))
	
	#list.sort()
	print list[0]
	print list
	
	#print min(0,0,'r')
	#print matrix
	#print steps
	
	# Try the 5*5 matrix and figure it out.
