#!/usr/bin/python

#The program power2.py takes a single non-negative integer as a command
#line argument and produces the powers of two that total to that
    #number.


import sys

#first calculate the number of terms

def power2(i):
    bs = [] #list of remainders after dividing by 2
    while (i > 0):
        r = i % 2
        bs.append(r) #adds the remainder to list bs, until you get to 1
        i = i >> 1 #divides i by 2 to give the next i
    print bs

#

    p = 1
    ps = []
    i = 0
    for b in bs:
        if (bs[i] == 1):
            ps.append(p)
        p = p * 2 # Do a power.
        i = i + 1 # Increment index
    nups = []
    # Cycle round the list.
    for p in ps:
        nups.insert(0, p)
    # Print the powers.
    for p in nups:
        print p
    return nups

if __name__ == '__main__':
    value = int(sys.argv[1])
    power2(value)