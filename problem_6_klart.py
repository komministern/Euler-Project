
if __name__ == '__main__':

	n = 100
	
	S_1 = (n*(n+1)/2) ** 2
	
	S_2 = 0
	for i in range(1, n+1):
		S_2 = S_2 + i ** 2
		
	print S_1 - S_2
	