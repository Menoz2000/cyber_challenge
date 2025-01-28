#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
# fin = open("input.txt", "r")  # Input file provided by the platform
# fout = open("output.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
fin = sys.stdin  # Input
fout = sys.stdout  # Output

def count_intervals(N, a):
    numeri_validi = []
    
    #find all triple (i,j,k)
    for num_index in range(len(a)):
        num = a[num_index]
        for i in range(len(a)):
            for j in range(i + 1, len(a)):  # i < j to avoid duplicated
                if a[i] * a[j] == num**2:
                    numeri_validi.append((i, j, num_index))
                    break

    print(numeri_validi)
    
    #set to memorize distinct intervals
    intervalli_distinti = set()
    print()
    
    #for each triple calculate distinct intervals
    for (i, j, num_index) in numeri_validi:
        #find min and max interval
        lmin = min(i, j, num_index)
        rmax = max(i, j, num_index)
        
        #add all sub-intervals
        for l in range(lmin + 1):
            for r in range(rmax, N):
                intervalli_distinti.add((l, r))

    print(intervalli_distinti)

    return len(intervalli_distinti)

T = int(fin.readline().strip())

for _ in range(T):
    N = int(fin.readline().strip())
    a = list(map(int, fin.readline().strip().split()))
    fout.write(str(count_intervals(N, a)) + "\n")
