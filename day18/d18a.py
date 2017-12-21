#!/usr/bin/python3
import sys
import collections
reg=collections.defaultdict(int)

f=open('input.txt')
#f=open('test.txt')
program = f.readlines()
progLinePtr=0
done=False

while not done:
    line = program[progLinePtr]

    try :
        (cmd,x,y)=line.strip('\n').split(' ')
    except ValueError:
        (cmd,x)=line.strip('\n').split(' ')

        
    Y = reg[y] if y.isalpha() else int(y)

    if cmd=='set':
        reg[x] = Y
    elif cmd=='add':
        reg[x]+= Y
    elif cmd=='mul':
        reg[x]*= Y
    elif cmd=='mod':
        reg[x]%= Y
    elif cmd=='rcv':
        if reg[x]!=0:
            reg[x]=reg['sound']
            print("First Recovery Sounds is {0:d}".format(reg[x]))
            quit()
    elif cmd=='jgz':
        if reg[x]>0:
            progLinePtr+= (Y-1)

    elif cmd=='snd':
        reg['sound']=reg[x]

    progLinePtr+=1;

