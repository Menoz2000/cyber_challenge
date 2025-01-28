#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
# fin = open("input.txt", "r")  # Input file provided by the platform
# fout = open("output.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
fin = sys.stdin  # Input
fout = sys.stdout  # Output


def execute_code(N, code):
    
    alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    alph_len = len(alph)

    #apply rotation
    def rotate_string(s, x):
        rotated = []
        for char in s:
            new_index = (alph.index(char) + x) % alph_len
            rotated.append(alph[new_index])
        return ''.join(rotated)

    #initial string
    current_string = ''

    #operations
    for op in code:

        if op.startswith('add '):
            #add char at the end
            added_char = op.split()[1]
            current_string += added_char

        elif op == 'del':
            #remove last char
            current_string = current_string[:-1]
        
        elif op.startswith('swap '):
            #swaw chars
            _, a, b = op.split()
            current_string = current_string.replace(a, "#").replace(b, a).replace("#", b)

        elif op.startswith('rot '):
            #rotate chars
            x = int(op.split()[1])
            current_string = rotate_string(current_string, x)

    return current_string    


N = int(fin.readline().strip())
code = []
#print (N)
for _ in range(N):
    s = fin.readline().strip()
    code.append(s)
#print (code)
print(execute_code(N, code))