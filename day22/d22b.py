#!/usr/bin/python3

import numpy as np

Nx=1001
Ny=1001
grid=np.zeros((Nx,Ny),dtype='uint8')

def show(grid,currentNode):
    for i in range(grid.shape[0]):
        print ('\n')
        for j in range(grid.shape[1]):
            print(' ' if ([i,j]-currentNode).any() else '[',end='')
            if grid[i,j]==0:
                print('.',end='')
            if grid[i,j]==1:
                print('W',end='')
            if grid[i,j]==2:
                print('F',end='')
            if grid[i,j]==3:
                print('#',end='')
            print(' ' if ([i,j]-currentNode).any() else ']',end='')
    print('\n')


#f=open('test.txt')
f=open('input.txt')

input=[l.strip('\n') for l in f.readlines()]
Xo=((grid.shape[0]-1)//2)-(len(input[0])-1)//2
Yo=((grid.shape[1]-1)//2)-(len(input)-1)//2


for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j]=='#':
            grid[Xo+i,Yo+j]=3

currentNode = np.array([ (grid.shape[0]-1)//2,  (grid.shape[1]-1)//2 ])
currentDir = 0
dirMap= [ [-1,0], [0,1], [1,0], [0,-1] ]
stateMap=['clean','weak','flag','infec']
infectionCount=0
#show(grid,currentNode)
for i in range(10000000):
    ndx=tuple(currentNode)
    if stateMap[int(grid[ndx])]=='clean':
        # Turn Left
        currentDir = (currentDir-1)%4
        # Become weakened
        grid[ndx]=1

    elif stateMap[int(grid[ndx])]=='weak':
        # Become infected
        grid[ndx]=3
        infectionCount+=1
        
    elif stateMap[int(grid[ndx])]=='flag':
        # Reverse
        currentDir = (currentDir+2)%4
        # Become clean
        grid[ndx]=0

    elif stateMap[int(grid[ndx])]=='infec':
        # Turn Right
        currentDir = (currentDir+1)%4
        # Become flagged
        grid[ndx]=2

    # Handle negative wrap on current Direction
    currentDir+= 4 if currentDir<0 else 0
    # Move
    currentNode += dirMap[currentDir]
    if (i%100000)==0:
        print("Percent Complete {0:f}".format(i/100000))
    #show(grid,currentNode)
print("Final Infection Count is {0:d}".format(infectionCount))

    

    
