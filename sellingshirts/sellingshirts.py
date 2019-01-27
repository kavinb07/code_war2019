#!/usr/bin/python

with open('sellingshirts.txt') as f:
    data = f.readlines()


print(float(data[0]) * 8 - 95)
