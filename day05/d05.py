#!/usr/bin/python3

f=open('input5a.txt')
mems=f.readlines()
mem = [int(i.strip()) for i in mems]

#mem=[0, 3, 0, 1, -3]

loc=0; cnt=0
while (loc<len(mem)):
    cnt+=1
    step=mem[loc]
    if (step>=3):
        mem[loc]-=1
    else:
        mem[loc]+=1
    loc+=step


print("Steps required are ",str(cnt))


