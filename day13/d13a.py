#!/usr/bin/python3

import numpy as np

f=open('input.txt')
data = f.readlines()
Nlayers=93

# Full map, negative numbers of unmonitored depths
depth   = -1*np.ones(Nlayers)
scanner = -1*np.ones(Nlayers)
move    = np.ones(Nlayers)

# Parse data
for line in data:
     (l,d)=line.strip('\n').split(':')
     depth[int(l)]=int(d)
     scanner[int(l)]=0;
 
cost=0
packet=0
while (packet<Nlayers):
     # Check for conflict with scanner
     if scanner[packet]==0:
          cost += packet*depth[packet]
          
     # Move scanner bots to next depth
     scanner= [s+m if (s>=0) else s for (s,m) in zip (scanner,move)]

     # Change move direction at end points
     move= [-1*m if ( s==(d-1) or s==0 ) else m for (s,m,d) in zip(scanner,move,depth)]

     packet+=1

print("The total cost is {0:d}".format(int(cost)))
     


     



     






