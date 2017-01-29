
from math import sqrt

if __name__ == '__main__':

	sum = 2 + 3 + 5

	list_of_primes = [2, 3, 5]
	
	nbr = 7
	
	while nbr < 2000000:
		
		i = 0
		prime = True
		
		while list_of_primes[i] <= int( sqrt( nbr ) ):
			if nbr % list_of_primes[i] == 0:
				prime = False
				break
			else:
				i += 1
		if prime:
			list_of_primes.append( nbr )
			sum += nbr
			
		nbr += 2
	
	print sum