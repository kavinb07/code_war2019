#!/usr/bin/python

with open('kepler.txt') as f:
    data = f.readlines()


for line in data:
    p = float(line.rstrip())
    if p == 0:
        break
    print((p**2)**(1.0/3))
