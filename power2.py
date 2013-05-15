#!/usr/bin/python

import sys

def power2(i):
    bs = []
    while (i > 0):
        r = i % 2
        bs.append(r)
        i = i >> 1 # Do a shift
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
