#!/usr/bin/python3
import numpy as np

input     =[76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229];
inputb_str='76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229';

#inputb_str='1,2,3'
#inputb_str='AoC 2017'
#inputb_str='1,2,3'
#inputb_str='1,2,4'

partB=True

msg  = [i for i in range(0,256)]
head=0
stepSize=0
L=len(msg)

if (partB):
    Nround=64;
    input=[]
    for i in range(0,len(inputb_str)):
        input.append(ord(inputb_str[i]))
    input+=[17,31,73,47,23]
else:
    Nround=1;

for round in range(0,Nround):
    for ndx in input:
        last = (head+ndx)
        if (last>L):
            flipvec = np.flipud(msg[head:L]+msg[0:last-L])
            for i in range(0,len(flipvec)):
                msg[(head+i)%(L)]= flipvec[i]
        else:
            flipvec = np.flipud(msg[head:last])
            msg[head:last] = flipvec;
        head+=(ndx+stepSize)
        head=head%L
        stepSize+=1

print("Solution for Part A is {0:d}".format(msg[0]*msg[1]))        

# XOR
sparse=[msg[i*16] for i in range(0,16)]
for i in range(0,16):
    for j in range(1,16):
        sparse[i]^=msg[i*16+j]

print("The solution for Part B is ",end='')
for i in range(0,16):
    print("%02x"%sparse[i],end='')

print("")
    
      
