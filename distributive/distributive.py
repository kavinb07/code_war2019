#!/usr/bin/python

with open('distributive.txt') as f:
    data = f.readlines()


a = data[0].rstrip()
b = data[1].rstrip()
c = data[2].rstrip()

print(a + ' x (' + b + ' + ' + c + ') = ' + a + ' x ' + b + ' + ' + a + ' + ' + c)
print(a + ' x ' + str(int(b) + int(c)) + ' = ' + str(int(a) * int(b)) + ' + ' + str(int(a) * int(c)))
print(str(int(a) * (int(b) + int(c))) + ' = ' + str(int(a) * (int(b) + int(c))))
