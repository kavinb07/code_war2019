#!/usr/bin/python

def delta(line_str):
    print line_str

with open("delta.txt", "r") as f:
    data_l = f.readlines()

line_num = 0
for lines in data_l:
    if line_num == 0:
        line_num = line_num + 1
        continue
    else:
        delta(lines)
        line_num = line_num + 1
