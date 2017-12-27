#!/usr/bin/python3

import numpy as np

Nx=501
Ny=501
grid=np.zeros((Nx,Ny))

def show(grid,currentNode):
    for i in range(grid.shape[0]):
        print ('\n')
        for j in range(grid.shape[1]):
            print(' ' if ([i,j]-currentNode).any() else '[',end='')
            print('.' if grid[i,j]==0 else '#',end='')
            print(' ' if ([i,j]-currentNode).any() else ']',end='')
    print('\n')


#f=open('test.txt')
f=open('input.txt')

input=[l.strip('\n') for l in f.readlines()]
Xo=((grid.shape[0]-1)//2)-(len(input[0])-1)//2
Yo=((grid.shape[1]-1)//2)-(len(input)-1)//2

print(input)
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j]=='#':
            grid[Xo+i,Yo+j]=1

currentNode = np.array([ (grid.shape[0]-1)//2,  (grid.shape[1]-1)//2 ])
currentDir = 0
dirMap= [ [-1,0], [0,1], [1,0], [0,-1] ]

infectionCount=0

for i in range(10000):
    ndx=tuple(currentNode)
    if grid[ndx]==1:
        currentDir = (currentDir+1)%4
    else:
        currentDir = (currentDir-1)%4
        infectionCount+=1

    currentDir+= 4 if currentDir<0 else 0 
    grid[ndx] = abs(grid[ndx]-1)
    currentNode += dirMap[currentDir]
#    show(grid,currentNode)
    print(infectionCount)
    


    

    
