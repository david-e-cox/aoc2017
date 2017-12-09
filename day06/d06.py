#!/usr/bin/python3

import numpy as np

#mem=[0,2,7,0]
mem=[2,8,8,5, 4,2,3,1, 5,5,1,2, 15,13,5,14]

stateHistory=set()
stateHistory.add(hash(str(mem)))

cnt=0
keyHash=0
done=False

while (not done):
    cnt+=1
    ndx=np.argmax(mem)
    buf=mem[ndx]
    mem[ndx]=0
    while (buf>0):
        ndx=(ndx+1)%len(mem)
        mem[ndx]+=1
        buf-=1

    curHash=hash(str(mem))
    if (curHash==keyHash): # Second Repeat
        done=True
        
    stateHistory.add(curHash)
    
    if ( len(stateHistory)==cnt):  # First Repeat
        cnt0=cnt
        keyHash=curHash

print ("The count is ",cnt0)
print ("The cycle length is ",cnt-cnt0)



        
    
    
