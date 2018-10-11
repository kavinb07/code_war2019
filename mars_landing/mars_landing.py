#!/usr/bin/python

with open("mars_landing.txt", "r") as f:
    data = f.readlines()

for numbers in data:
    number = numbers.split()
    m = int(number[0])
    v = int(number[1])
    p = m * v
    print p
