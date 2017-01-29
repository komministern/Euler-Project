#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock


def straight(nlst):
	if nlst[4] - nlst[3] == nlst[3] - nlst[2] == nlst[2] - nlst[1] == nlst[1] - nlst[0] == 1:
		return True
	else:
		return False
	
def flush(lst):
	if len(set([s[1] for s in lst])) == 1:
		return True
	else:
		return False
	
def	fourofakind(nlst):
	if nlst[0] == nlst[3] or nlst[1] == nlst[4]:
		return True
	else:
		return False
	
def fullhouse(nlst):
	if nlst[0] == nlst[1] == nlst[2] and nlst[3] == nlst[4] or nlst[0] == nlst[1] and nlst[2] == nlst[3] == nlst[4]:
		return True
	else:
		return False
	
def threeofakind(nlst):
	if nlst[0] == nlst[1] == nlst[2] or nlst[1] == nlst[2] == nlst[3] or nlst[2] == nlst[3] == nlst[4]:
		return True
	else:
		return False
		
def twopairs(nlst):
	if len(set(nlst)) == 3:
		return True
	else:
		return False
		
def onepair(nlst):
	if len(set(nlst)) == 4:
		return True
	else:
		return False
		
def eval(hand):
	numhand = sorted([cardvalue[card[0]] for card in hand])
	if flush(hand):
		if straight(numhand):
			return 13**5 * handvalue['straight flush'] + 13**4 * numhand[4]
		else:
			return 13**5 * handvalue['flush'] + 13**4 * numhand[4] + 13**3 * numhand[3] + 13**2 * numhand[2] + 13**1 * numhand[1] + 13**0 * numhand[0]
	else:
		if fourofakind(numhand):
			return 13**5 * handvalue['four of a kind'] + 13**4 * numhand[2]
		elif fullhouse(numhand):
			if numhand.count(numhand[0]) == 3:
				tripleval = numhand[0]
				pairval = numhand[4]
			else:
				tripleval = numhand[4]
				pairval = numhand[0]
			return 13**5 * handvalue['full house'] + 13**4 * tripleval + 13**3 * pairval
		elif straight(numhand):
			return 13**5 * handvalue['straight'] + 13**4 * numhand[4]
		elif threeofakind(numhand):
			if numhand[0] == numhand[2]:
				tripleval = numhand[0]
			elif numhand[1] == numhand[3]:
				tripleval = numhand[1]
			else:
				tripleval = numhand[2]
			numhand = [x for x in numhand if x != tripleval]
			return 13**5 * handvalue['three of a kind'] + 13**4 * tripleval
		elif twopairs(numhand):
			if numhand[0] == numhand[1]:
				lowpairval = numhand[0]
				numhand = [x for x in numhand if x != lowpairval]
				if numhand[0] == numhand[1]:
					highpairval = numhand[0]
					highcardval = numhand[2]
				else:
					highcardval = numhand[0]
					highpairval = numhand[2]
			else:
				highcardval = numhand[0]
				lowpairval = numhand[1]
				highpairval = numhand[3]
			return 13**5 * handvalue['two pair'] + 13**4 * highpairval + 13**3 * lowpairval + 13**2 * highcardval
		elif onepair(numhand):
			if numhand[0] == numhand[1]:
				pairval = numhand[0]
			elif numhand[1] == numhand[2]:
				pairval = numhand[1]
			elif numhand[2] == numhand[3]:
				pairval = numhand[2]
			elif numhand[3] == numhand[4]:
				pairval = numhand[3]
			numhand = [x for x in numhand if x != pairval]
			return 13**5 * handvalue['one pair'] + 13**4 * pairval + 13**3 * numhand[2] + 13**2 * numhand[1] + 13**1 * numhand[0]
		else:
			return 13**5 * handvalue['high card'] + 13**4 * numhand[4] + 13**3 * numhand[3] + 13**2 * numhand[2] + 13**1 * numhand[1] + 13**0 * numhand[0]
		



if __name__ == '__main__':

	handvalue = {'straight flush': 8, 'four of a kind': 7, 'full house': 6, 'flush': 5, 'straight': 4, 'three of a kind': 3, 'two pair': 2, 'one pair': 1, 'high card': 0}
	cardvalue = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
	
	hands = []
	
	f = open('./p054_poker.txt', 'r')
 
	hands = f.readlines()
	listofhands = []
	
	for each in hands:
		listofhands.append(each.translate(None, '\n').split())
	
	f.close()
	
	awin = 0
	
	for lst in listofhands:
		if eval(lst[0:5]) >= eval(lst[5:10]):
			awin += 1
			
	print awin
	
	
	
	