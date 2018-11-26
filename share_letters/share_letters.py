#!/usr/bin/python

with open('share_letters.txt') as f:
    data = f.readlines()


def find_shared(words):
    all_chars = []
    for word in words:
        for char in sorted(word):
            all_chars.append(char)
    select = []
    words[0] = list(words[0])
    words[1] = list(words[1])
    words[2] = list(words[2])
    for char in sorted(all_chars):
        if char in words[0] and char in words[1] and char in words[2]:
            select.append(char)
            words[0][words[0].index(char)] = ''
            words[1][words[1].index(char)] = ''
            words[2][words[2].index(char)] = ''
    result = ''
    for char in select:
        result += char
    print result


triplets = int(data[0])
for i in range(1, triplets + 1):
    current_strings = data[i].upper().split()
    find_shared(current_strings)
