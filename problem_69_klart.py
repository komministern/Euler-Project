#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock
from math import factorial, sqrt


# Ojojoj. Denna funktion tar så mycket tid att det är löjligt [O(n2)]?.
# Lösbart med någon form av sieve kanske?

#def phi(n):
#    divisors = []
#    j = 0
#    for i in range(2,n):
#        if i not in divisors:
#        
#            if n % i != 0:
#                j += 1
#            else:
#                k = i
#                while k < n:
#                    divisors.append(k)
#                    k += i
#    return j + 1

    
        
# Denna lösning mycket bättre, men någon form utav sieve är nog att föredraga!
        
def phi(n):
    
    p = 1.0 * n
    
    i = 2
    while i**2 <= n:
        if n % i == 0:
            p = p - p / i
            while n % i == 0:
                n /= i
        i += 1 
    if n > 1:
        p = p - p / n
    
    return int(p)
    

if __name__ == '__main__':
    
    maxq = 0
    maxi = 0
    
    for i in range(2,1000001):
        
        q = 1.0 * i / phi(i)
        
        if q > maxq:
            maxq = q
            maxi = i
        
                
    print maxi, maxq 

    
