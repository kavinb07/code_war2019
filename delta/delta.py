#!/usr/bin/python

def delta(line_str):
    list_deltas = []
    num = line_str.split()
    for iter in range(1, len(num) - 1):
        diff = int(num[iter + 1]) - int(num[iter])
        list_deltas.append(-diff)

    first_val = int(num[1])
    string_line = str(first_val)
    for delta_value in list_deltas:
        first_val = first_val + delta_value
        string_line = string_line + " " + str(first_val)
    print string_line



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
