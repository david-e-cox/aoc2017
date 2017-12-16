#!/usr/bin/python3
import binascii
import numpy as np

#key='flqrgnkx'
key='uugsqrei'

def knothash(input_str):
    msg  = [i for i in range(0,256)]
    strmap={'f':'1111','e':'1110','d':'1101','c':'1100','b':'1011','a':'1010','9':'1001','8':'1000',\
            '7':'0111','6':'0110','5':'0101','4':'0100', '3':'0011','2':'0010','1':'0001','0':'0000'}
    head=0
    stepSize=0
    L=len(msg)

    Nround=64;
    input=[]
    for i in range(0,len(input_str)):
        input.append(ord(input_str[i]))
    input+=[17,31,73,47,23]
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
    # XOR
    sparse=[msg[i*16] for i in range(0,16)]
    for i in range(0,16):
        for j in range(1,16):
            sparse[i]^=msg[i*16+j]
    hexstr=""
    binstr=""
    for i in range(0,16):
        tmp="%02x"%sparse[i]
        hexstr+=tmp
        one,two=tmp
        binstr+=strmap[one]
        binstr+=strmap[two]
    return(hexstr,binstr)                


def tagNeighboors(grid,groupCnt,px,py):
    grid[px,py]=groupCnt
    about = [ (1,0), (-1,0), (0,1), (0,-1) ]

    for xy in about:
        lx=min(max(xy[0]+px,0),127)
        ly=min(max(xy[1]+py,0),127)
        if grid[(lx,ly)]==0:
            grid = tagNeighboors(grid,groupCnt,lx,ly)
    return(grid)


total=0
groupCnt=0;
done=False

grid=np.zeros((128,128),dtype='int')

for i in range(128):
    hexstr,binstr=knothash('{0:s}-{1:d}'.format(key,i))
    total+=binstr.count('1')
    for j in range(len(binstr)):
        grid[i,j]=int(binstr[j])-1
print('Total Count is {0:d}'.format(total))


while not done:
    px,py = np.where(grid==0)
    if len(px)==0:
        done=True
        continue
    groupCnt+=1;
    grid  = tagNeighboors(grid,groupCnt,px[0],py[0])
print('Total Group Count is {0:d}'.format(groupCnt))

