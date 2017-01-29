#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock


def f(a, b):
    return a*(a+1)*b*(b+1) - 8e6

if __name__ == '__main__':
    
    minimum = 1e9
    minab = (0,0)
    
    a = 1
    b = 1
    
    while f(a, b) < 0:
        
        while f(a, b) < 0:
            b += 1
            
        if abs(f(a,b)) < minimum:
            minimum = abs(f(a,b))
            minab = (a,b)
            print a, b, minimum, a*(a+1)*b*(b+1)/4
        
        
        if abs(f(a,b-1)) < minimum:
            minimum = abs(f(a,b-1))
            minab = (a,b-1)
            print a, b, minimum, a*(a+1)*b*(b-1)/4
        
        a += 1
        b = 1
        
    print minab, minab[0]*minab[1]