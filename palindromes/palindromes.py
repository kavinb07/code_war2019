#!/usr/bin/python

# import regex
import re
regex = re.compile('[^a-zA-Z]')

with open("palindromes.txt", "r") as f:
    data = f.readlines()


# checks if a string is a palindrome
def palindrome(string):
    return regex.sub('', string).upper() == regex.sub('', string[::-1]).upper()


def find_palindrome(string):
    # These next lines contain variables used to hold the longest palindrome
    # current longest palindrome
    longest = ''
    # the current palindrome in processing
    current = ''
    for i in range(len(string)):
        current = ''
        if string[i].isalpha():
            for j in range(i, len(string)):
                current += string[j]
                if palindrome(string[i:j + 1]) is True:
                    if len(string[i:j + 1]) > len(longest) and string[j].isalpha():
                        longest = string[i:j + 1]
    if len(longest) > 1:
        print longest
    else:
        print 'NO PALINDROME'


total_strings = int(data[0])
for i in range(1, total_strings + 1):
    find_palindrome(data[i].rstrip())
