#!/usr/bin/python

with open('disassemble.txt') as f:
    data = f.readlines()


special_strings = [
    'zero', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight', 'nine', 'ten'
]

print('Number ' + str(special_strings[int(data[0])]) + ' is alive!')
