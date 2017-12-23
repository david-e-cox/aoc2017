#!/usr/bin/python3
import sys
import collections
reg=collections.defaultdict(int)

f=open('input.txt')
#f=open('test.txt')
program = f.readlines()
progLinePtr=0
done=False
progId=int(sys.argv[1])
reg['p']=progId
sendCnt=0
recvCnt=0
while not done:
    line = program[progLinePtr]

    try :
        (cmd,x,y)=line.strip('\n').split(' ')
    except ValueError:
        (cmd,x)=line.strip('\n').split(' ')
        y=x
        
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
        tmp=''
        while(len(tmp)==0):
            tmp=sys.stdin.readline().strip('\n')
        reg[x]=int(tmp)
        recvCnt+=1
    elif cmd=='jgz':
        Xcond = reg[x] if x.isalpha() else int(x)
        if Xcond>0:
            progLinePtr+= (Y-1)
    elif cmd=='snd':
        print("{0:d}".format(reg[x]),file=sys.stdout,flush=True)
        sendCnt+=1

    progLinePtr+=1;
    print("Prog{:d} Sent:{:d} Recv:{:d}".format(progId,sendCnt,recvCnt),file=sys.stderr)
