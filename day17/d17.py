#!/usr/bin/python3

step=335

cbuffer=[0]
cbuffer_len=1

pos=0
pctDone=0

for count in range(1,50000001):
    pos+=step
    pos%=cbuffer_len
    cbuffer_len+=1
    if (pos<2018):
        cbuffer.insert(pos+1,count)
    pos+=1
    if (pos>=cbuffer_len):
        pos-=cbuffer_len

    if count==2017:
         print("Following 2017 is {0:d}".format(cbuffer[(pos+1)%cbuffer_len]))

    if (count%5000000==0):
        pctDone+=10
        print("  Percent Done: {0:d}/100".format(pctDone))
        
print("Following Zero is {0:d}".format(cbuffer[1]))

    
