#!/usr/bin/env python

if __name__ == '__main__':
    
    n = 2 ** 1000
    sum = 0
    
    while n >= 10:
        sum += n % 10
        n /= 10

    sum += n
    
    print sum