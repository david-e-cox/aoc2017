#!/usr/bin/python3
import numpy as np

f=open('input.txt')
Nlayers=93

#f=open('test.txt')
#Nlayers=7

data = f.readlines()
depth   = -1*np.ones(Nlayers)
for line in data:
     (l,d)=line.strip('\n').split(':')
     depth[int(l)]=int(d)

done=False
delay=0
# No need to check every layer, only ones with active scanners
checkLanes = [i for i,val in enumerate(depth) if val > 0 ]

while not done:
     delay+=1
     hit=0
     for i in checkLanes:
          if depth[i]>0:
               # Check if at this depth the scanner will be at zero
               # Its modulo a longer list(2N-2), going out and back
               if ((delay+i)%(2*depth[i]-2)==0): 
                    hit=1;
                    continue
     if (delay%10000)==0:
          print("Zero cost delay is more than {0:d}".format(delay))

     if (hit==0):
          print("The zero cost delay is {0:d}".format(delay))
          done=True


     


     



     






