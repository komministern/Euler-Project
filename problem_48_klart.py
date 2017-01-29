#!/usr/bin/env python


if __name__ == '__main__':

	sum = 0
	for i in range(1, 1001):
		sum += i ** i
	
	string = str(sum)
	
	print string[-10:]
	
	