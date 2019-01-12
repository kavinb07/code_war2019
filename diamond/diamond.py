#!/usr/bin/python

with open('diamond.txt') as f:
    data = f.readlines()


def make_diamond(size):
    matrix = []
    for i in range(1, (size / 2) + 1):
        string = ''
        string += '#' * (size / 2 - i)
        string += '/' * i
        string += '\\' * i
        string += '#' * (size / 2 - i)
        matrix.append(string)

    for i in reversed(range(1, (size / 2) + 1)):
        string = ''
        string += '#' * (size / 2 - i)
        string += '\\' * i
        string += '/' * i
        string += '#' * (size / 2 - i)
        matrix.append(string)
    return matrix


for line in data:
    values = line.split()
    size = int(values[0])
    if size == 0:
        break
    cols = int(values[1])
    rows = int(values[2])
    matrix = make_diamond(size)
    for i in range(cols):
        for line in matrix:
            print(line * rows)
