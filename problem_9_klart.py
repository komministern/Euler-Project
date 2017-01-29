
if __name__ == '__main__':

	found = False
	a = 0
	
	while not found and a < 1000:
		a += 1
		b = 1
		while not found and b < 1000:
			c = 1000 - a - b
			if c**2 - a**2 - b**2 == 0:
				found = True
			else:
				b += 1
		
	if found:
		print 'a =', a
		print 'b =', b
		print 'c =', c
	else:
		print 'No triplet!'