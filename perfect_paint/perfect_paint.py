#!/usr/bin/python

with open('perfect_paint.txt') as f:
    data = f.readlines()


def calc_cubes(l, w, h):
    total = l * w * h
    unpainted = (l-2) * (w-2) * (h-2)
    painted = total - unpainted
    more_less = ''
    dimension_string = str(l) + 'x' + str(w) + 'x' + str(h)
    if painted > unpainted:
        more_less = 'MORE'
    elif painted < unpainted:
        more_less = 'LESS'
    elif painted == unpainted:
        print 'A ' + dimension_string + ' block is PERFECT.'
        return None
    print 'A ' + dimension_string + ' block is ' + more_less + ' than Perfect.'


for line in data:
    values = line.split()
    if values.count('0') == 3:
        break
    else:
        calc_cubes(int(values[0]), int(values[1]), int(values[2]))
