#!/usr/bin/python3

cnta=0;
cntb=0;

for phrase in open('input4.txt'):
    words=phrase.split()
    if (len(set(words)) == len(words)):  # no repeats in passphrase
        cnta+=1
        scramble=set();
        for s in words:
            scramble.add(''.join(sorted(s)))
        if len(scramble) == len(words): # no anagrams in passphrase
            cntb+=1;

print("The number of valid passphrases is ",cnta)
print("The number of strong passphrases is ",cntb)

    
