#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
# fin = open("input.txt", "r")  # Input file provided by the platform
# fout = open("output.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
fin = sys.stdin  # Input
fout = sys.stdout  # Output


def find_key(L, s):
    lettere_trovate = set()
    contatore = 0

    for lettera in s:
        if lettera not in lettere_trovate:
            lettere_trovate.add(lettera)
            contatore += 1

        if contatore == 25:
            for l in "abcdefghijklmnopqrstuvwxyz":
                if l not in lettere_trovate:
                    return l
    
    return None

N = int(fin.readline().strip())

for _ in range(N):
    L = int(fin.readline().strip())
    s = fin.readline().strip()
    print(find_key(L, s))