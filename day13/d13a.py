#!/usr/bin/python3

import numpy as np

f=open('input.txt')
data = f.readlines()
Nlayers=93

# Full map, negative numbers of unmonitored depths
depth   = -1*np.ones(Nlayers)
scanner = -1*np.ones(Nlayers)
move    = np.ones(Nlayers)
history = np.zeros(Nlayers)

# Import data
for line in data:
     (l,d)=line.strip('\n').split(':')
     depth[int(l)]=int(d)
     scanner[int(l)]=0;
 
cnt=0
cost=0
packet=-1
done=False

while (cnt<Nlayers):
     packet+=1

     # Check for conflict with scanner
     if scanner[packet]==0:
          cost += packet*depth[packet]
          
     # Move scanner bots to next depth, reverse direction at limits (0,depth)
     for loc in range(len(scanner)):
          if scanner[loc]>=0:
               scanner[loc]+=move[loc]

     # Change move direction at end points     
     move= [-1*move if ( loc==(depth-1) or loc==0 ) else move for (loc,move,depth) in zip(scanner,move,depth)]

     cnt+=1

print("The total cost is {0:d}".format(int(cost)))
     


     



     






