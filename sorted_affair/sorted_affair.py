#!/usr/bin/python3

import operator

with open('sorted_affair.txt') as f:
    data = f.readlines()


teams = {}
# populate teams
for line in data:
    if line.rstrip() == '0 0':
        break
    teams['a' + line.split()[0]] = 0

# add up points
for line in data:
    if line.rstrip() == '0 0':
        break
    values = line.split()
    team = values[0]
    points = int(values[1])
    teams['a' + team] += points


ranks = [{'name': 'q', 'score': 0}, {'name': 'q', 'score': 0},
         {'name': 'q', 'score': 0}, {'name': 'q', 'score': 0},
         {'name': 'q', 'score': 0}]
for team, points in reversed(sorted(teams.items(), key=operator.itemgetter(1))):
    for i in range(len(ranks)):
        if points > ranks[i]['score']:
            ranks[i]['name'] = team
            ranks[i]['score'] = points
            break


for i in range(len(ranks)):
    string = ''
    string += str(i + 1) + ' '
    string += ranks[i]['name'][1:5] + ' '
    string += str(ranks[i]['score'])
    print(string)
