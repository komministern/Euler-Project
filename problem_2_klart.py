

if __name__ == '__main__':
	
# Brute force

	sum = 2
	n = 0
	n_1 = 2
	n_2 = 1

	while n < 4000000:
		n = n_1 + n_2
		if n % 2 == 0:
			sum += n
		n_2 = n_1
		n_1 = n

	print( sum )
