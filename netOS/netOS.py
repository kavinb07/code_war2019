#!/usr/bin/python

with open('netOS.txt') as f:
    data = f.readlines()


for line in data:
    values = line.split()
    w = int(values[0])
    l = int(values[1])
    if w == 0 and l == 0:
        break
    print(w * l)
