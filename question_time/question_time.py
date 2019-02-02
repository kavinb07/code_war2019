#!/usr/bin/python

with open('question_time.txt') as f:
    data = f.readlines()


def get_time(min):
    hour_pos = 60 - min
    hour = hour_pos / 5
    if min < 10:
        min = str(0) + str(min)
    return str(hour) + ':' + str(min)


for line in data:
    if int(line) == -1:
        break
    print(get_time(int(line)))
