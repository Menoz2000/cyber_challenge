#!/bin/env python3

import sys

# Decomment here if you want to read to/write from file
# fin = open("input.txt", "r")  # Input file provided by the platform
# fout = open("output.txt", "w")  # Output file to submit

# Decomment here to read to/write from command line
fin = sys.stdin  # Input
fout = sys.stdout  # Output


def find_sum_of_times(N, M, t, f, emails):
    total_arr_time = 0

    for em_time in emails:
        current_time = em_time

        for i in range(N):
            #attend the next multiple of t[i]
            if current_time % t[i] != 0:
                current_time += t[i] - (current_time % t[i])

            #add delay
            current_time += f[i]

        #sum
        total_arr_time += current_time

    return total_arr_time



N, M = map(int, fin.readline().strip().split())
t = list(map(int, fin.readline().strip().split()))
f = list(map(int, fin.readline().strip().split()))
emails = list(map(int, fin.readline().strip().split()))

print(find_sum_of_times(N, M, t, f, emails))