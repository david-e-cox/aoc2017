#!/usr/bin/python3
import numpy

f=open('input.txt');
#f=open('test.txt');

# List for rows, char string indexing for cols.
map=f.readlines()

# Position has the horizontal and vertical coordinates
pos={'horz':map[0].find('|'),'vert':0}

# Direction is current direction of travel
direction='vert'

#Sense is +1 for down/right, -1 for up/left
sense=1

# Letters found along the way
found=[]

done=False
stepCnt=0

while not done:
    stepCnt+=1
    symbol=map[pos['vert']][pos['horz']]

    if (symbol=='|' or symbol=='-'):
        pos[direction]+=sense

    elif (symbol=='+'):
        # Look for path to the left, if not turn right
        if (direction=='vert'):  
            if (map[pos['vert']][pos['horz']+sense]==' '):
                sense*=-1
            direction='horz'
            pos[direction]+=sense
        else:   
            if (map[pos['vert']+sense][pos['horz']]==' '):
                sense*=-1
            direction='vert'
            pos[direction]+=sense

    elif (symbol==' '):
        done=True

    else:  # Found a letter, store
        found.append(symbol)
        pos[direction]+=sense

print("The letter map is {0:s}".format("".join(found)))
print("The packet travelled {0:d} steps".format(stepCnt-1))




