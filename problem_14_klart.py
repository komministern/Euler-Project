

def iterate(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3*n + 1

list_of_start_values = [0] * 1000001

def iterations(n):
	if n == 1:
		return 1
	elif n > 1000000:
		counter = 1
		while n > 1:
			n = iterate(n)
			counter += 1
		return counter
	elif list_of_start_values[n] == 0:
		list_of_start_values[n] = 1 + iterations(iterate(n))
		return list_of_start_values[n]
	else:
		return list_of_start_values[n]

if __name__ == '__main__':
	
	longest_chain = 0
	for i in range(2, 1000000):
		if iterations(i) > longest_chain:
			longest_chain = iterations(i)
			start_number = i
	
	print start_number, longest_chain
	
