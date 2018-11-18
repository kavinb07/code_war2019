#!/usr/bin/python

with open('scientific_notation.txt', 'r') as f:
    data = f.readlines()


def get_decimal(num, exp):
    decimal = num * (10 ** exp)
    return format(decimal, '.2f')


for line in data:
    values = line.split()
    num = float(values[0])
    exp = int(values[1])
    if num == 0 and exp == 0:
        break
    else:
        print get_decimal(num, exp)
