#!/usr/bin/python3

factorA = 16807
factorB = 48271

divisor = 2147483647

genA = int(722*factorA)
genB = int(354*factorB)
Nmatch=0;
Nsamples=0;
while (Nsamples<40000000):
    Nsamples+=1
    if ( (genA&0xFFFF) == (genB&0xFFFF) ):
        Nmatch+=1
        print("{0:32b}  {1:32b}".format(genA,genB))
    genA*=factorA
    genB*=factorB
    genA=genA%divisor
    genB=genB%divisor

print("Total Match Count is {0:d}".format(Nmatch))
