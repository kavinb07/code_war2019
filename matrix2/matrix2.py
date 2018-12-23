#!/usr/bin/python

with open('matrix2.txt') as f:
    data = f.readlines()


matrix1 = []
matrix2 = []
final_matrix = []

def print_matrix(matrix):
    for row in matrix:
        display = ''
        for char in row:
            display += str(char)
        print(display)


rows = int(data[0].split()[0])
cols = int(data[0].split()[1])

for i in range(rows):
    row = []
    for j in range(cols):
        row.append('*')
    matrix1.append(row)
    matrix2.append(row)
    final_matrix.append(row)


set1 = data[1].split()
set2 = data[2].split()

row = 0
col = 0

for i in range(rows * cols):
    if i % rows == 0 and i != 0:
        row += 1
        col = 0
    matrix1[row][col] = int(set1[i])
    col += 1

print_matrix(matrix1)
print('=' * 3)
row = 0
col = 0

for i in range(rows * cols):
    if i % rows == 0 and i != 0:
        row += 1
        col = 0
    matrix2[row][col] = int(set2[i])
    col += 1


print_matrix(matrix2)
print('=' * 3)

row = 0
col = 0

for i in range(rows * cols):
    if i % rows == 0 and i != 0:
        row += 1
        col = 0
    final_matrix[row][col] = int(set1[i]) + int(set2[i])
    col += 1

print_matrix(final_matrix)
