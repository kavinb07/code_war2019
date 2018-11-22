#!/usr/bin/python

with open("cryptography.txt", "r") as f:
    data = f.readlines()


def clean_noise(string, n):
    # string is the actual text while n is the noise threshold
    all_chars = sorted(set(string))
    for char in all_chars:
        if string.count(char) >= n:
            # if the current char appears more than n times, remove it
            string = filter(lambda a: a != char, string)
    # string has now been cleaned of excessive characters
    return string


# get some data from the first line of data
search_data = data[0].split()
row_count = int(search_data[0])
noise_thres = int(search_data[2])
# get some data from the second line of data
word_data = data[1].split()
word_count = int(word_data[0])
word_lengths = []
# make an array containing the lengths of each word
for i in range(1, len(word_data)):
    word_lengths.append(int(word_data[i]))

master_string = ''
for i in range(2, row_count + 2):
    for char in data[i].rstrip():
        if char != ' ' and char.isalpha():
            master_string += char
# get a string with all unnecessary characters removed
cleaned_string = clean_noise(master_string, noise_thres)
# decoded_message will hold the final string
decoded_message = ''
current_char = 0
for i in range(len(word_lengths)):
    if i == 0:
        decoded_message += cleaned_string[:word_lengths[i]]
        current_char = word_lengths[i]
    else:
        decoded_message += ' ' + cleaned_string[current_char:current_char + word_lengths[i]]
        current_char += word_lengths[i]
print decoded_message
