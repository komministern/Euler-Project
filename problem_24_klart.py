#!/usr/bin/env python

def next_lexographic_permutation(list):
	ind = len(list) - 1
	while ind > 0:
		if list[ind - 1] < list[ind]:
			
			# Find the index for the smallest digit in list[ind:] greater than list[ind - 1]
			
			highest_digit = 9
			for i in range(ind, len(list)):
				if list[i] > list[ind - 1] and list[i] <= highest_digit:
					highest_digit = list[i]
					swap_ind = i
					
			# Swap the elements in the index found and list[ind - 1]
			
			temp = list[ind - 1]
			list[ind - 1] = list[swap_ind]
			list[swap_ind] = temp

			# Sort the tail, list[ind:]
			
			list_tail = list[ind:]
			
			list_tail.sort()
			
			for i in range( len(list_tail) ):
				list.pop()
			list.extend(list_tail)
			
			break
			
		else:
			ind -= 1
	return list

if __name__ == '__main__':
	
	list = [0,1,2,3,4,5,6,7,8,9]
	
	for i in range(999999):
		list = next_lexographic_permutation(list)
	
	print list