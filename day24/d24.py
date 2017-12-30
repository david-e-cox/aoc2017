#!/usr/bin/python3
import collections
import copy

# Peter Norvig (https://github.com/norvig/pytudes/) and I had similar ideas here
# His code worked, and mine didn't...... so we decied to just use his ;)
def mkbridge(bridge,matching,size):
    if len(bridge)>0:
        yield(bridge)
    for pipe in matching[size]:
        if pipe not in bridge:
            if pipe[0]==size:
                nextPipe=pipe[1]
            elif pipe[1]==size:
                nextPipe=pipe[0]
            else:
                print("Should not happen...")
            tmp=copy.deepcopy(bridge)
            tmp.append(pipe)
            yield from mkbridge(tmp,matching,nextPipe)

def score(bridge):
    total=0
    for t in bridge:
        total+=t[0]+t[1]
    return(total)


#f=open('test.txt')
f=open('input.txt')

matching = collections.defaultdict(set)
input=[i.strip('\n').split('/') for i in f.readlines()]

#Create tuples for each pipe in a dictionary keyed by its end sizes
for p in input:
    #snum=(min([int(p[0]),int(p[1])]),max([int(p[0]),int(p[1])]))
    pnum=(int(p[0]),int(p[1]))
    matching[pnum[0]].add(pnum)
    matching[pnum[1]].add(pnum)                                                                                                                                                           

strength=[]
length=[]
for i in mkbridge([],matching,0):
    strength.append(score(i))
    length.append(len(i))
    
print("The max strength is {0:d}".format(max(strength)))
maxL=max(length)
for i in range(len(length)):
    if length[i]==maxL:
        print("The max length is {0:d} with strength {1:d}".format(maxL,strength[i]))
    

    
    
   
