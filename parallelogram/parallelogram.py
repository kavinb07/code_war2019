#!/usr/bin/python

with open('parallelogram.txt', 'r') as f:
    data = f.readlines()


def print_shape(string):
    strlen = len(string)
    for i in range(strlen + 1):
        current = ''
        current += ' ' * (strlen - i)
        current += string[strlen - i:]
        print current
    for i in range(1, strlen):
        print string[i:]


words = int(data[0])
for i in range(1, words + 1):
    print_shape(data[i].rstrip())
