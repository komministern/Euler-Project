
from math import sqrt

def get_first_n_primes(n):
	list_of_primes = [2, 3, 5]
	nbr = 7
	while len( list_of_primes ) < n:
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
	return list_of_primes

def nbr_of_divisors(n, list_of_primes):
	
	list_of_divisors = []

	i = 0
	while n > 1:
		if n % list_of_primes[i] == 0:
			list_of_divisors.append(list_of_primes[i])
			n /= list_of_primes[i]
		else:
			i += 1
	
	nbr_of_divisors = 1
	while len( list_of_divisors ) > 0:
		prime = list_of_divisors[0]
		nbr_of_prime = list_of_divisors.count(prime)
		nbr_of_divisors *= (nbr_of_prime + 1)
		for each in range(nbr_of_prime):
			list_of_divisors.remove(prime)
	
	return nbr_of_divisors


def triangular_number(n):
	return n*(n+1)/2

if __name__ == '__main__':

	nbr_of_primes_in_list = 1000

	primes = get_first_n_primes(nbr_of_primes_in_list)
	
	i = 1
	while nbr_of_divisors(triangular_number(i), primes) < 500:
		i += 1
		if i > primes[-1]:
			nbr_of_primes_in_list *= 10
			primes = get_first_n_primes(nbr_of_primes_in_list)

	print triangular_number(i), '(=', i, '*', i+1, '/ 2) has', nbr_of_divisors(triangular_number(i), primes), 'divisors.'
	