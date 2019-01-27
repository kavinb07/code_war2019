#!/usr/bin/python

with open('counting_ones.txt') as f:
    data = f.readlines()


def get_ones(n):
    string = ''
    for i in range(0, n + 1):
        string += str(i)
    return string.count('1')


for line in data:
    if int(line) == -1:
        break
    print(get_ones(int(line)))
