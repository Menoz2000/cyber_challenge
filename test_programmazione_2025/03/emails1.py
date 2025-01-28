#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
# fin = open("input.txt", "r")  # Input file provided by the platform
# fout = open("output.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
fin = sys.stdin  # Input
fout = sys.stdout  # Output


def find_sum_of_times(N, M, t, f, emails):
    total_arrival_time = 0

    #precompute
    for email_time in emails:
        current_time = email_time

        for i in range(N):
            t_i, f_i = t[i], f[i]
            remainder = current_time % t_i
            
            #calculate next reminder
            if remainder != 0:
                current_time += (t_i - remainder)

            #add delay
            current_time += f_i

        total_arrival_time += current_time

    return total_arrival_time

N, M = map(int, fin.readline().strip().split())
t = list(map(int, fin.readline().strip().split()))
f = list(map(int, fin.readline().strip().split()))
emails = list(map(int, fin.readline().strip().split()))

fout.write(str(find_sum_of_times(N, M, t, f, emails)) + '\n')