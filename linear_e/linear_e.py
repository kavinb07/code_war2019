#!/usr/bin/python

with open('linear_e.txt') as f:
    data = f.readlines()


grid_data = data[0].split()
left = 0
right = int(grid_data[0]) + 1
top = 1
bottom = int(grid_data[1]) - 1

message = ''

while left < right and top < bottom:
    for i in range(top, bottom):
        message += data[i][left]
    left += 1
    for i in range(left, right + 1):
        message += data[bottom - 1][i]
    bottom -= 1
    for i in reversed(range(top, bottom)):
        message += data[i][right]
    right -= 1
    for i in reversed(range(left, right + 1)):
        message += data[top][i]
    top += 1


reversed_message = ''
for char in reversed(message):
    reversed_message += char
print reversed_message.split()[0]
