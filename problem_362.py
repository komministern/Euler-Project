
from math import sqrt, factorial

def list_of_primes_below(limit):
	list_of_primes = [2, 3, 5]
	nbr = 7
	while nbr < limit:
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

def factor_histogram(n):
	histogram = []
	latest_prime_index = -1
	prime_index = 0

	while n > 1:
		if n % primes[prime_index] == 0:
			n /= primes[prime_index]
			if prime_index != latest_prime_index:
				latest_prime_index = prime_index
				histogram.append(1)
			else:
				histogram[-1] += 1
		else:
			prime_index += 1
			if prime_index == len(primes):
				histogram.append(1)
				n = 1
	return histogram

def Fsf(n):
	list = factor_histogram(n)
	return 1 + factorial(len(list)) / 2


if __name__ == '__main__':
	
	primes = list_of_primes_below( long( sqrt( 10000000000 ) ) + 1 )
	
	print Fsf(54)
	
	sum = 0
	for i in range(2, 101):
		sum += Fsf(i)
	
	print sum
	
	print Fsf(30)
	
	
	# Fsf(2*3*5) = 2*3*5 + 6*5 + 2*15 + 3*10 [4]
	# Fsf(2*2*3*5) = 2*2*3*5 + 2*6*5 + 2*2*15 + 2*3*10 + 6*10 [5]
	# Fsf(2*2*2*3*5) = [5]
	
	# Fsf(2*2*3*3*5) = 2*3*2*3*5 + 2*3*6*5 + 2*3*3*10 + 2*2*3*15 + 2*6*15 + 2*6*30 = [6]
	
	
	