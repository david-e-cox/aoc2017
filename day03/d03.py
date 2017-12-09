#!/usr/bin/python3

import numpy as np

print("\nPart A:")

stepLength=0;  # grows each turn
stepSign=-1;   # flips each xy move pair
x=0;y=0;cnt=1; 
target=361527
done=False

while (not done):
    stepLength+=1;
    stepSign*=-1;
    # Move along X-axis in direction of stepSign
    x+=stepSign*stepLength;
    cnt+=stepLength;
    if (cnt>target):  # check for solution
        x-=stepSign*(cnt-target)
        print("Hit Target at ",x,y)
        print("City Block Distance is ",abs(x)+abs(y))
        done=True
    # Move along Y-axis in direction of stepSign
    y+=stepSign*stepLength;
    cnt+=stepLength;
    if (cnt>target and not done): # check for solution
        y-=stepSign*(cnt-target)
        print("Hit Target at ",x,y);
        print("City Block Distance is ",abs(x)+abs(y))
        done=True

print("\nPart B:")

done=False
stepLength=0;
stepSign=-1;

x=0;y=0;cnt=1;
target=361527;

offset=int(4); # 0,0 is middle of memory array, using an offset for indexing

mem=np.zeros((2*offset+2,2*offset+2));
mem[offset][offset]=1

while (not done):
    stepLength+=1;
    stepSign*=-1;
    for ix in range(x+stepSign, x + stepSign*stepLength + stepSign,stepSign):
        val=0;
        # Loop through all neighbors, sum values
        for nx in [-1,0,1]:
            for ny in [-1,0,1]:
                val+=mem[ix+offset+nx][y+offset+ny]
        # Assign current point to sum of neighbors        
        mem[ix+offset][y+offset]=val;
        if (val>target and not done): # check for solution
            print("Target Reached at ",ix,y)
            print("Value is ",val)
            done=True
    # Jumping to end of movement line in X        
    x+=stepSign*stepLength;
    
    for iy in range(y + stepSign,y + stepSign*stepLength +stepSign,stepSign):
        val=0;
        # Assign current point to sum of neighbors        
        for nx in [-1,0,1]:
            for ny in [-1,0,1]:
                val+=mem[x+offset+nx][iy+offset+ny]
        mem[x+offset][iy+offset]=val;
        if (val>target and not done): # check for solution
            print("Target Reached at ",ix,y);
            print("Value is ",val)
            done=True;
    # Jumping to end of movement line in Y        
    y+=stepSign*stepLength

# Debug, print matrix check with test case
#np.set_printoptions(precision=2,suppress=True)        
#print(str(np.flipud(np.transpose(mem))))



    
            
        
    
    

    



        


