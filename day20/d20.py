#!/usr/bin/python3
import re
import numpy as np

f=open('input.txt')
#f=open('test.txt')

# must be a better way...
exp='<([-+]?\\d+),([-+]?\\d+),([-+]?\\d+)>'
sexp="".join(['p=', exp,', v=',exp,', a=',exp])

pos=[]
vel=[]
acc=[]

for line in f.readlines():
    m=re.match(sexp,line)
    pos.append([int(m.group(1)),int(m.group(2)),int(m.group(3))])
    vel.append([int(m.group(4)),int(m.group(5)),int(m.group(6))])
    acc.append([int(m.group(7)),int(m.group(8)),int(m.group(9))])

#Use numpy for addition
P=np.array(pos)
V=np.array(vel)
A=np.array(acc)
for i in range(500):
    V+=A
    P+=V
    D=np.abs(P[:,0]) + np.abs(P[:,1]) + np.abs(P[:,2])
    print("Particle {0:d} is closest".format(np.argmin(D)))


P=np.array(pos)
V=np.array(vel)
A=np.array(acc)
for i in range(50):
    V+=A
    P+=V
    rowKill=[]
    # numpy's "unique" almost works here, but leaves one of the particles from each collision
    # not clear how to determine from numpy output how man collisions there were
    # Slow direct implementation below
    for row in range(np.size(P,0)):
        for other in range(row+1,np.size(P,0)):
            if max(abs(P[row,:]-P[other,:]))==0:
                rowKill.append(row)
                rowKill.append(other)
    keepNdx=np.setdiff1d(range(0,np.size(P,0)),rowKill);
    P=P[keepNdx,:]
    V=V[keepNdx,:]
    A=A[keepNdx,:]

    print("Particles remaining {0:d}".format(np.size(P,0)))



    
