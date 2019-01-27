#!/usr/bin/python

with open('tribonacci.txt') as f:
    data = f.readlines()


tribonacci = [0, 1, 1]
for i in range(3, 100):
    tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])


for line in data:
    if int(line) == -1:
        break
    print(tribonacci[int(line)])
