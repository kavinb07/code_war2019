#!/usr/bin/python

from math import *

with open('ballistic.txt') as f:
    data = f.readlines()


v = float(data[0])
angle = float(data[1])
radians = angle * pi / 180

print(v**2 * sin(2 * radians) / 9.80665)
