#!/usr/bin/python

with open('sorted_affair.txt') as f:
    data = f.readlines()


ranks = {}

for line in data:
    if line.rstrip() == '0 0':
        break
    ranks['a' + line.split()[0]] = 0


for line in data:
    if line.rstrip() == '0 0':
        break
    values = line.split()
    team = values[0]
    points = int(values[1])
    ranks['a' + team] += points


print(ranks)
