#!/usr/bin/python

with open('distinct_letters.txt') as f:
    data = f.readlines()


def check_distinct(word):
    letters = set(sorted(list(word)))
    for letter in letters:
        if word.count(letter) > 1:
            return False
    return True


for line in data:
    line = line.rstrip()
    if line == '.':
        break
    distinct = check_distinct(line)
    result = ''
    if distinct is True:
        result = 'USES DISTINCT LETTERS'
    else:
        result = 'DOES NOT USE DISTINCT LETTERS'
    print(line + ' ' + result)
