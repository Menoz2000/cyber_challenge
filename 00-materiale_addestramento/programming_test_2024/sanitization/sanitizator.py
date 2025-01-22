'''
CyberChallenge.IT 2024 - Programming Test
CyberChallenge.IT 2024
Programming Test
Sanitization [40 points]
Problem Statement
Alan Good afternoon, everyone, and welcome to the inaugural lecture of CyberChallenge.IT 2024! I’m
Alan, your guide through the fabulous world of hacking! Let’s kick off with a little magic trick!
Alan opens a web page, types some peculiar characters in an input field, and... Boom!
A cascade of user data appears publicly!
Bob Whoa! You just broke the internet!
Alan Not the whole internet, Bob. That was just a dummy website with fake data prepared for the lecture.
But what can we learn from it?
Bob That most of the internet is broken?
Charlie That some inputs can be dangerous?
Alan Spot on, Charlie! So, your first task for the day is crafting a kind of sanitizer! You’ll receive a list of
banned words and a set of input strings. For each string, simply type SAFE or BANNED, depending on
whether the corresponding input contains banned words.
Bob But wasn’t this course about hacking?
Meanwhile, Charlie starts typing...
Problem Details
Input
The input consists of N + M + 1 lines:
 Line 1: two space-separated integers, N and M
 Lines 2, . . . , M + 1: the list of banned words, one per line
 Lines M + 2, . . . , M + N + 1: the list of input strings, one per line
Both banned words and inputs are composed only of lowercase letters, uppercase letters and digits. In particular,
they do not contain spaces. Their length is variable between 3 and 20 characters.
Output
The output consists of N lines. Print either SAFE if the corresponding input string does not contain any of the
banned words, or BANNED if it contains at least one of them.
'''

# read input
import sys
input = sys.stdin.read
data = input().splitlines()

# first line contains N and M
N, M = map(int, data[0].split())

# next M lines contain banned words
banned_words = set(data[1:M + 1])
#print(banned_words)

# following N lines are input strings to check
input_strings = data[M + 1:M + 1 + N]

# output results
for string in input_strings:
    if any(banned in string for banned in banned_words):
        print("BANNED")
    else:
        print("SAFE")