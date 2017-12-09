#!/usr/bin/python3

import numpy as np
print("\nPart A:");
#data=[[5,1,9,5],[7,5,3],[2,4,6,8]]
data=np.loadtxt('input_day2a.txt','int')

diffSum=0
for i in range(0,len(data)):
    diffSum+=np.amax(data[i])-np.amin(data[i])
print(diffSum)
    
print("\n\nPart B:")
#data=[[5,9,2,8],[9,4,7,3],[3,8,6,5]]
data=np.loadtxt('input_day2b.txt','int')

diffSum=0;
for k in range(0,len(data)):
    row=data[k]    
    for i in range(0,len(row)-1):
        for j in range(i+1,len(row)):
            if ((row[i]%row[j])==0 or (row[j]%row[i])==0 ):
                diffSum+=np.max([row[i]/row[j],row[j]/row[i]])
print(diffSum)
            
        
    
    

    



        


