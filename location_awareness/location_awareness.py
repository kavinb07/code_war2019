#!/usr/bin/python

with open('location_awareness.txt') as f:
    data = f.readlines()


def get_location(s1, s2, s3):
    min_error = 50000
    x = None
    y = None
    for i in range(-100, 101):
        for j in range(-100, 101):
            # solve for the P for s1
            d1 = ((0.0-i)**2+(100.0-j)**2) ** 0.5
            P1 = s1 * (d1**2)
            # solve for P2
            d2 = ((-100.0-i)**2+(-100.0-j)**2) ** 0.5
            P2 = s2 * (d2**2)
            # solve for P3
            d3 = ((100.0-i)**2+(-100.0-j)**2) ** 0.5
            P3 = s3 * (d3**2)
            average_power = (P1 + P2 + P3) / 3
            e1 = abs(average_power - P1)
            e2 = abs(average_power - P2)
            e3 = abs(average_power - P3)
            total_error = e1 + e2 + e3
            if total_error < min_error:
                min_error = total_error
                x = i
                y = j
    print str(x) + ' ' + str(y)


for line in data:
    values = line.split()
    s1 = float(values[0])
    s2 = float(values[1])
    s3 = float(values[2])
    if s1 == 0 and s2 == 0 and s3 == 0:
        break
    get_location(s1, s2, s3)
