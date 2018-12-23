#!/usr/bin/python

with open('matrix1.txt') as f:
    data = f.readlines()


matrix = []

rows = int(data[0].split()[0])
cols = int(data[0].split()[1])

for i in range(rows):
    row = []
    for j in range(cols):
        row.append('*')
    matrix.append(row)


def print_matrix(matrix):
    for row in matrix:
        display = ''
        for char in row:
            display += char
        print(display)


numbers = data[1].split()
row = 0
col = 0

for i in range(len(numbers)):
    if i % rows == 0 and i != 0:
        row += 1
        col = 0
    matrix[row][col] = numbers[i]
    col += 1


print_matrix(matrix)
