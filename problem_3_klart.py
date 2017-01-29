

if __name__ == '__main__':

	p = 600851475143
	
	while p != 1:
		n = 3
		while p % n != 0:
			n += 2
		p = p / n
	
	print n
	

