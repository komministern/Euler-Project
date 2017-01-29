#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock


def sqdig(n):
    
    i = 0
    
    while n > 0:
        i += (n%10) ** 2
        n = n / 10
    
    return i



if __name__ == '__main__':

    n = 10000000

    lst = [0] * (n + 1)
    lst[1] = 1
    lst[89] = 89
    
    
    for i in range(1,n + 1):
        
        if lst[i] == 0:
            
            j = i
            while True:
                
                j = sqdig(j)
                
                if lst[j] != 0:
                    lst[i] = lst[j]
                    break
                    
    print len([1 for i in lst if i==89])