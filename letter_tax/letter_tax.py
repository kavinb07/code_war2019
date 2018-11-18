#!/usr/bin/python

with open('letter_tax.txt', 'r') as f:
    data = f.readlines()


def tax_string(string, n):
    new_string = ''
    for j in range(len(string)):
        if j % n != 0:
            new_string += string[j]
    return new_string


string_count = int(data[0])
for i in range(1, string_count + 1):
    values = data[i].split()
    n = int(values[0])
    string = values[1].rstrip()
    print tax_string(string, n)
