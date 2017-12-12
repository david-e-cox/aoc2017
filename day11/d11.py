#!/usr/bin/python3
import numpy as np

f=open('input.txt')
stream=f.read().strip('\n').split(',')

#stream=['ne','ne','ne']
#stream=['se','sw','se','sw','sw']

# Using axial coordinates(non-orthogonal:45 deg offset), [+north,+northEast]
qrMap={'n':[1,0],'s':[-1,0],'ne':[0,1],'se':[-1,1],'nw':[1,-1],'sw':[0,-1]}

qr=np.zeros(2)
distMax=0
for move in stream:
    qr += qrMap[move]
    # See, https://www.redblobgames.com/grids/hexagons/
    cube=[qr[0], -qr[0]-qr[1], qr[1]]
    dist=(abs(cube[0])+abs(cube[1])+abs(cube[2]))/2
    distMax=max([distMax,dist])

print (" Distance is {0:f}".format(dist))
print (" Max Distance is {0:f}".format(distMax))    
    

