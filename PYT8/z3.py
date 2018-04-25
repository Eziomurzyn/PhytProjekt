#!/usr/bin/env python

import sys

def isFirst(n):
    dividers=0
    for i in range(2,n):
        if(n%i==0):
            dividers+=1
    if(dividers==0):
        return True
    else:
        return False

def rozklad(n):
    liczba=n
    prime=2
    li=[]
    while(liczba>1):
        if(isFirst(prime)):
            times=0
            while(liczba%prime==0):
                times+=1
                liczba/=prime
            if(times>0):
                k=(prime,times)
                li.append(k)
        prime+=1
    return li


n=int(sys.argv[1])

print(rozklad(n))
        
