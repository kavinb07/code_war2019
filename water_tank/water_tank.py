#!/usr/bin/python

# open data file
with open('water_tank.txt', 'r') as f:
    data = f.readlines()


def get_weeks(water_per_week):
    return int(10000/water_per_week)


for line in data:
    per_week = int(line)
    if per_week != 0:
        print str(per_week) + ' gallons per week will last ' + str(get_weeks(per_week)) + ' weeks'
    else:
        break
