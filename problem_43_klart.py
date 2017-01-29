#!/usr/bin/env python

#from numpy import *
#from string import *
#from time import clock
#from math import sqrt
from itertools import permutations

if __name__ == '__main__':

	l = list(map("".join, permutations('0123456789')))
	plist = []

	for item in l:
		
		if int(item[1:4]) % 2 == 0:
			if int(item[2:5]) % 3 == 0:
				if int(item[3:6]) % 5 == 0:
					if int(item[4:7]) % 7 == 0:
						if int(item[5:8]) % 11 == 0:
							if int(item[6:9]) % 13 == 0:
								if int(item[7:10]) % 17 == 0:
									plist.append(int(item))
	
	print sum(plist)
	
	# Gudars vilken ful losning. Jag skams lite. Gjutjarn..