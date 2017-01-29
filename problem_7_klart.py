
from math import sqrt

if __name__ == '__main__':

	list_of_primes = [2, 3, 5]
	
	nbr = 7
	
	while len( list_of_primes ) < 10001:
		
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
			
		nbr += 2
	
	print list_of_primes[-1]