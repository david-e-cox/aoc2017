#!/usr/bin/python3

reg = {'a':1,'b':0,'c':0,'d':10,'e':0,'f':0,'g':0,'h':0}
mulCount=0
linePtr=0

f=open('input.txt')
prog=f.readlines()
done=False

while not done:
    try:
        line=prog[linePtr]
    except IndexError:
        print("Line Multiply Count is {0:d}".format(mulCount))
        print("Register H contins {0:d}".format(reg['h']))
        quit()

    (cmd,x,y)=line.strip('\n').split(' ')
    Y= reg[y] if y.isalpha() else int(y)
    if cmd=='set':
        reg[x] = Y
    elif cmd=='sub':
        reg[x] -= Y
    elif cmd=='mul':
        reg[x] *= Y
        mulCount+=1
    elif cmd=='jnz':
        Xcond = reg[x] if x.isalpha() else x
        if (Xcond!=0):
            linePtr+=(Y-1)

    linePtr+=1
    #print(linePtr)
    if (linePtr==14):
            print("{0:d} {1:d} {2:d} {3:d}   {4:d} {5:d} {6:d} {7:d}".\
            format(reg['a'],reg['b'],reg['c'],reg['d'],reg['e'],reg['f'],reg['g'],reg['h']))
            
    
            
            
