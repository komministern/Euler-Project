#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt




if __name__ == '__main__':
	
	list = []
	
	for a in range(2, 101):
	
		for b in range (2, 101):
		
			list.append(a ** b)
			
	list.sort()
	
	new_list = []
	new_list.append(list[0])
	
	for each in list:
		if each != new_list[-1]:
			new_list.append(each)
	
	print len(new_list)
	
	print len(set([a ** b for a in range(2, 101) for b in range(2, 101)]))