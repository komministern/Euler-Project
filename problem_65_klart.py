#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock





if __name__ == '__main__':

    #coeffs = [1,2,1,1,4]#,1,1,6,1,1,8,1]

    n = 99
    coeffs = []
    i = 1
    j = 1
    while len(coeffs) < n:
        if j%(i*3 - 1) == 0:
            coeffs.append(i*2)
        elif j%(i*3) == 0:
            coeffs.append(1)
            i += 1
        else:
            coeffs.append(1)
        j += 1


    #print coeffs

    t = 1
    n = coeffs[-1]
    coeffs = coeffs[:-1]

    while len(coeffs) > 0:
        
        newt = n
        newn = coeffs[-1]*n + t
        
        t = newt
        n = newn
        coeffs = coeffs[:-1]
        
    print t+2*n, n
    
    nbr = t+2*n
    n = 0
    
    while nbr > 0:
        n += nbr%10
        nbr = nbr/10
        
    print n