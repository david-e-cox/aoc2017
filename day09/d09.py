#!/usr/bin/python3

#stream='{}'
#stream='{{{}}}'
#stream='{{},{}}'
#stream='{{{},{},{{}}}}'
#stream='{<a>,<a>,<a>,<a>}'
#stream='{{<ab>},{<ab>},{<ab>},{<ab>}}'
#stream='{{<!!>},{<!!>},{<!!>},{<!!>}}'
#stream='{{<a!>},{<a!>},{<a!>},{<ab>}}'
#stream='<{o"i!a,<{i<a>';

f=open('input.txt')
stream=f.read()

depth =0
groups=0
score =0
gCnt  =0

inData   =False
inGarbage=False
nextSkip =False

for c in stream:
    if nextSkip:
        nextSkip=False
        continue

    if c=='!':
        nextSkip=True
        continue

    if not inGarbage:
        if c=='<':
            gCnt-=1 # Offset +1 later, as here we enter garbage state
            inGarbage=True
        if c=='{':
            groups+=1
            if inData:
                depth+=1
            inData=True
        if c=='}':
            score+=(depth+1);
            depth-=1

    if c=='>' and inGarbage:
        inGarbage=False

    if inGarbage:
        gCnt+=1;
        

print ("Groups is "+str(groups))
print ("Score is "+str(score))
print ("Garbage Count is "+str(gCnt))        
        
    
    
