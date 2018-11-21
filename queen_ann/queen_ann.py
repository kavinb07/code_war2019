#!/usr/bin/python

# open data file
with open('queen_ann.txt', 'r') as f:
    data = f.readlines()


def check_word(word):
    likes_word = False
    for i in range(len(word)):
        if i < len(word) - 1:
            if word[i] == word[i + 1]:
                likes_word = True
    if likes_word is True:
        return 'likes '
    else:
        return 'hates '


words_for_check = int(data[0])
for i in range(1, words_for_check + 1):
    print str(check_word(data[i])) + data[i].rstrip()
