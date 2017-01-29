


if __name__ == '__main__':

	primes = [2, 3, 5, 7, 11, 13, 17, 19]
	occurances = [0] * len(primes)

	for i in range(2, 21):
		
		for j in range(8):
			
			p = i
			n = 0
			while p % primes[j] == 0:
				n += 1
				p = p / primes[j]
			
			if occurances[j] < n:
				occurances[j] = n
	
	s = 1		
	for i in range(len(primes)):
		s = s * (primes[i] ** occurances[i])
	
	print s