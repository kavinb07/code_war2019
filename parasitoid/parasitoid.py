#!/usr/bin/python

with open('parasitoid.txt') as f:
    data = f.readlines()


print(int(data[0]) * int(data[1]))
