#!/usr/bin/python3
import sys
f=open('input.txt')
#f=open('test.txt')

# Sometimes code exists only to show how things shouldn't be done.
# Below is such code.  Time spent figuring it out, is time wasted.

# Create connection dictionary
con={}
for connection in f.readlines():
    (pstr,vstr)=connection.split('<->')
    con[int(pstr)]=[int(value) for value in vstr.split(',')]

# Create grouping for each program
group = [set() for i in range(len(con))]

cnt=0
totalP=0
accountedFor=set()

for i in range(len(group)):
    group[i].add(i)
    lenOldGroup=0;
    while(len(group[i])!=lenOldGroup): # Iterate until no additional paths
        lenOldGroup=len(group[i])       
        for program in con.keys():
            for via in con[program]:
                # If one of the connected programs in in the return-to-zero group
                # then add this program to that group
                if (via in group[i]) and (program not in accountedFor):
                    accountedFor.add(program)
                    group[i].add(program)
                    #if the group has grown, re-iterate through all the programs    

# Calculate number of groups, gathered by lowest member program                    
for i in range(len(group)):
    if (len(group[i])>1):
        totalP+=len(group[i])
        cnt+=1
# Some programs only talk to themselves, add missing solo groups        
cnt+= (len(con)-totalP)
        
print(" Number of return paths to zero is {0:d}".format(len(group[0])))
print(" Total number of groups is {0:d}".format(cnt))


 
        

    
