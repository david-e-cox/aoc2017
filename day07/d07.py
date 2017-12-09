#!/usr/bin/python3

f=open('input7.txt');

#Hashes
wt=dict();
totalWt=dict();
stack=dict();

#Sets
level0=set();
level1=set();
level2=set();
level3=set();
level4=set();
level5=set();

for line in f.readlines():
    line=line.strip()
    words=line.split()
    wt.update({words[0]:int(words[1].strip('()'))})
    if len(words)>2:
        list=[]
        for item in words[3:len(words)]:
            list.append(item.strip(','))
        stack.update({words[0]:list})
    if len(words)<3:
        level0.add(words[0])

# all disks except those in level0        
levelnZ = set(wt.keys()) - level0

# level1 Disks one step from level0
for disk in levelnZ:
    for ref in stack[disk]:
        if ref in level0:
            level1.add(disk)

# level2 Disks two steps from level0
for disk in levelnZ-level1:
    for ref in stack[disk]:
        if ref in level1:
            level2.add(disk)

# level3 Disks three steps from level0
for disk in levelnZ-level1-level2:
    for ref in stack[disk]:
        if ref in level2:
            level3.add(disk)

# level4 Disks four steps from level0
for disk in levelnZ-level1-level2-level3:
    for ref in stack[disk]:
        if ref in level3:
            level4.add(disk)

print(len(wt))
print(len(level0))            
print(len(level1))
print(len(level2))
print(len(level3))
print(len(level4))
# This has the singular root, solution to part A
print("Solution to part A is "+str(level4))
print("")


# Recursive function to calculate cumlative stack weight
def stackWt(key,total,level0,wt):
    total+=wt[key]
    if key in stack.keys():
        for others in stack[key]:
            total+=int(stackWt(others,0,level0,wt))
    return(total)


for key in stack.keys():
    totalWt.update({key:stackWt(key,0,level0,wt)})

print("Steps to part B Solution:(manual find)")
# Manual discover, go down until un-balanced path
# until it is balanced, the step back one and fix
# it's individual weight
#for disk in level4:
#for disk in ['gjxqx']:
for disk in ['yruivis']:
#for disk in ['sphbbz']:
    for ref in stack[disk]:
        if ref in totalWt.keys():
            print("ref: "+str(ref)+"\tWeight "+str(totalWt[ref]))
        else:
            print("ref: "+str(ref)+"\tWeight "+str(wt[ref]))


    
