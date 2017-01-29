#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from numpy import *
#from string import *
#from time import clock




if __name__ == '__main__':

    m = 0
    i = 1
    j = 1

    
    while j <= 1000:
        while len(str(i ** j)) <= j:   
    
            if len(str(i ** j)) == j:
                m += 1
        
            i += 1
        
        i = 1    
        j += 1
        
    print m
    
    # För lat för att visa övre gräns för sökning.