#!/usr/bin/python3
import time
prog='a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p'.split(',')
#prog='a,b,c,d,e'.split(',')
progOrig=prog[:]

Np=len(prog)

def xchange(prog,n1,n2):
    tmp=prog[n1]
    prog[n1]=prog[n2]
    prog[n2]=tmp
    return(prog)

def partner(prog,l1,l2):
    n1=n2=-1
    for pos,char in enumerate(prog):
        if char==l1:
            n1=pos
        elif char==l2:
            n2=pos
        elif (n1>=0 and n2>=0):
            continue
    return(xchange(prog,n1,n2))

def spin(prog,count):
    pbuf=prog[:]
    start=(Np-count)
    for i in range(Np):
        pbuf[i] = prog[(i+start)%Np]
    return(pbuf)

f=open('input.txt')
dance = f.read().strip('\n').split(',')
#dance = ['s1','x3/4','pe/b']

for doOver in range(100):
    for move in dance:
        if move[0]=='x':
            n1,n2=move[1:].split('/')
            prog=xchange(prog,int(n1),int(n2))
        elif move[0]=='p':
            l1,l2=move[1:].split('/')
            prog=partner(prog,l1,l2)
        elif move[0]=='s':
            prog=spin(prog,int(move[1:]))

    if (doOver==0):
        print("Pattern after one round is {0:s}".format("".join(prog)))
    if (prog==progOrig):
            print("  Note: Repeat in pattern at {0:d}".format(doOver))
    if (doOver == (1e9%30-1)):
            print("Pattern after a billion rounds wil be {0:s}".format("".join(prog)))

