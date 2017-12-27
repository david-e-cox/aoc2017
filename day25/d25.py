#!/usr/bin/python3
import numpy as np

done=False
tape=np.zeros((10001),dtype='uint8')
ptr=5000
state='A'
prog={'A':{'writ':[1,0],'move':[+1,-1],'jump':['B','B']}, \
      'B':{'writ':[0,1],'move':[+1,-1],'jump':['C','B']}, \
      'C':{'writ':[1,0],'move':[+1,-1],'jump':['D','A']}, \
      'D':{'writ':[1,1],'move':[-1,-1],'jump':['E','F']}, \
      'E':{'writ':[1,0],'move':[-1,-1],'jump':['A','D']}, \
      'F':{'writ':[1,1],'move':[+1,-1],'jump':['A','E']}  \
      }

progCnt=0
done=False
while not done:
    cVal=tape[ptr]
    tape[ptr]=prog[state]['writ'][cVal]
    ptr     +=prog[state]['move'][cVal]
    state    =prog[state]['jump'][cVal]

    progCnt+=1
    if progCnt>=12629077:
        done=True
        
print("The checksum is {0:d}".format(tape.sum()))
      

