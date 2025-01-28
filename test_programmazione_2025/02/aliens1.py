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
    alph_map = {char: idx for idx, char in enumerate(alph)}
    alph_len = len(alph)

    #apply rotation
    def rotate_string(s, x):
        x %= alph_len
        return ''.join(alph[(alph_map[char] + x) % alph_len] for char in s)

    #initial string (using list)
    current_string = []

    #operations
    for op in code:

        if op.startswith('add '):
            #add char at the end
            added_char = op[4:]
            current_string.append(added_char)

        elif op == 'del':
            #remove last char
            if current_string:
                current_string.pop()
        
        elif op.startswith('swap '):
            #swaw chars
            _, a, b = op.split()
            current_string = [b if char == a else a if char == b else char for char in current_string]

        elif op.startswith('rot '):
            #rotate chars
            x = int(op[4:])
            current_string = list(rotate_string(current_string, x))

    return ''.join(current_string)


N = int(fin.readline().strip())
code = [fin.readline().strip() for _ in range(N)]
fout.write(execute_code(N, code) + '\n')
