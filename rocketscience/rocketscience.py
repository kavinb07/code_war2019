#!/usr/bin/python

with open('rocketscience.txt') as f:
    data = f.readlines()


print(float(data[0]) * 28.3495)
