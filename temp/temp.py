#!/usr/bin/python

with open("temp.txt", "r") as f:
    data = f.readlines()


def get_temp(t, t0, t1, c0, c1):
    m = (c1 - c0) / (t1 - t0)
    b = c0 - (m * t0)
    return ((m * t) + b) / 8.0


lines = int(data[0])
for i in range(1, lines + 1):
    all_data = data[i].split()
    t = float(all_data[0])
    t0 = float(all_data[1])
    t1 = float(all_data[2])
    c0 = float(all_data[3])
    c1 = float(all_data[4])
    print str(get_temp(t, t0, t1, c0, c1))
