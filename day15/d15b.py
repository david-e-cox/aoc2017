#!/usr/bin/python3

factorA = 16807
factorB = 48271
divisor = 2147483647

#genA = int(65*factorA)
#genB = int(8921*factorB)
genA = int(722*factorA)
genB = int(354*factorB)

Nmatch=0;
Nsamples=0;
keeperA=keeperB=-1;

while (Nsamples<5000000):
    if genA%4==0:
        keeperA=genA
    if genB%8==0:
        keeperB=genB

    #If new vaues on both generators, do comparison    
    if (keeperA>=0) and (keeperB>=0):
        Nsamples+=1
        if ( (keeperA & 0xFFFF) == (keeperB & 0xFFFF) ):
            Nmatch+=1
        # Reset keepers to restore generation    
        keeperA=keeperB=-1  
        
    # Just keep swiming, just keep swimming...
    if (keeperA<0):
        genA*=factorA
        genA=genA%divisor

    if (keeperB<0):    
        genB*=factorB
        genB=genB%divisor
        
print("Total Match Count is {0:d}".format(Nmatch))
