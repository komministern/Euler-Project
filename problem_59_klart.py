#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock


def decipher(listofascii, key):
	
	s = ''
	i = 0
	
	for ascii in listofascii:
		s += chr(ascii ^ ord(key[i]))
		i += 1
		if i == len(key):
			i = 0
	
	return s


if __name__ == '__main__':

	
	f = open('./p059_cipher.txt', 'r')
	s = f.readline()
	f.close()
	
	listofascii = []
	
	listofstr = s.split(',')
	
	[listofascii.append(int(s)) for s in listofstr]
		
		
	chars = 'abcdefghijklmnopqrstuvwxyz'
	foundkey = ''
		
	for c1 in chars:
		for c2 in chars:
			for c3 in chars:
				key = c1 + c2 + c3
				text = decipher(listofascii, key)
				if 'the' in text and 'was' in text and 'not' in text:
					foundkey = key
	
	
	sum = 0
	for c in decipher(listofascii, foundkey):
		sum += ord(c)
		
	print sum
	
	