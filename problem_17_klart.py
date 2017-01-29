#!/usr/bin/env python

if __name__ == '__main__':
	
	digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	
	sum = 0
	
	m = 1
	while m < 1000:
		str = ''
		n = m
		if n >= 100:
			str += digits[(n / 100) - 1] + 'hundred'
			if n % 100 != 0:
				str += 'and'
		n = n % 100
		if n != 0:
			if n / 20 == 0:
				str += digits[(n % 20) - 1]
			else:
				str += tens[(n / 10) - 2]
				if n % 10 != 0:
					str += digits[(n % 10) - 1]
		print str
		sum += len(str)
		m += 1
	
	sum += len('one') + len('thousand')
	
	print sum