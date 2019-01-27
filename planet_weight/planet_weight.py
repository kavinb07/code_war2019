#!/usr/bin/python

with open('planet_weight.txt') as f:
    data = f.readlines()


for line in data:
    values = line.split()
    name = values[0]
    if name == 'END':
        break
    weight = float(values[1])
    planet = values[2]
    conversion = float(values[3])
    print('On ' + planet + ', ' + name + ' would weigh ' + str(weight * conversion) + ' pounds.')
