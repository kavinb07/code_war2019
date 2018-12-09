#!/usr/bin/python

from math import ceil

with open('dirtyard.txt') as f:
    data = f.readlines()


l = float(data[0]) / 3
w = float(data[1]) / 3
h = float(data[2]) / 3

print(int(ceil(l * w * h)))
