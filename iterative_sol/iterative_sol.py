#!/usr/bin/python

def calc_y(array, sol_array):
    values = array.split()
    A = float(values[1])
    B = float(values[2])
    C = float(values[3])
    M = float(values[4])
    N = float(values[5])
    error = float(values[6])
    x_i = C + (A * sol_array + M) / (B * sol_array + N)
    return x_i



with open("iterative_sol.txt", "r") as f:
    data_lines = f.readlines()

line_num = 0
for line_item in data_lines:
    if line_num == 0:
        line_num = line_num + 1
        continue
    else:
        line_num_array = line_item.split()
        y_previous = []
        y_previous.append(float(line_num_array[0]))
        y_prev = float(line_item[0])
        error = line_num_array[6]
        for loop_iter in range(1, 21):
            y_prev = calc_y(line_item, y_prev)
            y_previous.append(y_prev)
        for loop_iter in range(1, 21):
            diff = y_previous[loop_iter] - y_previous[loop_iter - 1]
            if diff < 0:
                diff = diff * -1
            if diff < error:
                print "converging"
                break
