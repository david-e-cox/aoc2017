#!/usr/bin/python3
import numpy as np

f=open('input.txt')
#f=open('test.txt')
rules=[rule.strip('\n') for rule in f.readlines()]
ruleD={}
for r in rules:
    tmpList=r.split('=>')
    ruleD[tmpList[0].strip(' ')] = tmpList[1].strip(' ')
    
pat0=np.array([ [0,1,0],[0,0,1],[1,1,1] ],dtype=int);

def pat2str(pattern):
    str=''
    for row in range(pattern.shape[0]):
        for col in range(pattern.shape[1]):
            str+='#' if pattern[row][col] else '.'
        str+='/'
    return str.strip('/')

def str2pat(string):
    cnt=0
    size=string.find('/')
    pat=np.zeros((size,size),dtype=int)
    for row in range(size):
        for col in range(size):
            if string[cnt]=='#':
                pat[row][col]=1
            cnt+=1
        cnt+=1
    return pat

def mkrot(pat):
    P=[]
    P.append(pat)
    P.append(np.rot90(P[0]))
    P.append(np.rot90(P[1]))
    P.append(np.rot90(P[2]))
    P.append(np.fliplr(P[0]))
    P.append(np.fliplr(P[1]))
    P.append(np.fliplr(P[2]))
    P.append(np.fliplr(P[3]))
    return P

def breakUp(bigPat,nSkip):
    colStride=0
    gridList=[]
    eBlockSize=np.shape(bigPat)[0]
    for i in range (0,eBlockSize,nSkip):
        for j in range(0,eBlockSize,nSkip):
            gridList.append(bigPat[i:i+nSkip,j:j+nSkip])
        colStride+=1
    return gridList,colStride


for round in range(18):
    # BreakUp into smaller blocks
    if (np.shape(pat0)[0]%2==0):
        gridList,colStride = breakUp(pat0,2)
    else:
        gridList,colStride = breakUp(pat0,3)

    # Peform substitutions for matching rules            
    for ndx in range(len(gridList)):
        if (np.shape(gridList[ndx])[0]==2) or (np.shape(gridList[ndx])[0]==3):
            for psimilar in mkrot(gridList[ndx]):
                if pat2str(psimilar) in ruleD.keys():
                    gridList[ndx]=str2pat(ruleD[pat2str(psimilar)])
                    continue

    # Reshape into single large pattern
    N=0
    rowCnt=0
    offsetRow=0
    offsetCol=0
    for p in gridList:
        N+=np.shape(p)[0]
    pat0=np.zeros((N//colStride,N//colStride))
    for i in range(len(gridList)):
        (m,n)=gridList[i].shape
        pat0[offsetRow:offsetRow+m,offsetCol:offsetCol+n]=gridList[i]
        if (i+1)%colStride==0:
            offsetRow+=n
            offsetCol=0
        else:
            offsetCol+=m

    print("In round {0:d} the total count is {1:d}".format(round+1,np.count_nonzero(pat0)))
                

    
    
    
