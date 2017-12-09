#!/usr/bin/python3

import collections

f=open('input.txt')
#f=open('test.txt')

code = f.readlines()
reg=collections.defaultdict(int)
maxRun=0
for line in code:
    [regOut,pm,value,ifstr,regCond,op,valueCond]=line.split()
    if (eval('reg["'+regCond+'"] '+op+valueCond)):
        if pm=='inc':
            reg[regOut]+=int(value)
        else:
            reg[regOut]-=int(value)
    maxRun=max([maxRun,max([value for key,value in reg.items()])])

print("Max Final Value is "+str(max([value for key,value in reg.items()])))
print("Max Running Value is "+str(maxRun))




        

    
