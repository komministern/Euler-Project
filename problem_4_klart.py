
from math import sqrt

if __name__ == '__main__':

	found = False

	for i in range(9, 0, -1):
		if found == True:
			break
		else:
			for j in range(9, -1, -1):
				if found == True:
					break
				else:
					for k in range(9, -1, -1):
						palindrome = 100000*i + 10000*j + 1000*k + 100*k + 10*j + 1*i
						for l in range(int( sqrt(palindrome) ), 100, -1):
							if palindrome % l == 0 and palindrome / l <= 999:
								print palindrome, '=', l, '*', palindrome / l
								found = True
								break


