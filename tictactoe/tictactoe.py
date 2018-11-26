#!/usr/bin/python

with open('tictactoe.txt') as f:
    data = f.readlines()


def get_winner(string):
    string = list(string)
    winner_found = False
    for i in range(1, 4):
        # check if a user won horizontally
        if len(set(string[(3 * i) - 3:3 * i])) == 1:
            winner_found = True
            print 'Player ' + string[(3 * i) - 1] + ' won.'
            for j in range((3 * i) - 3, (3 * i)):
                string[j] = '$'
            break
        elif len(set(
            (string[i - 1]) + (string[i + 2] + (string[i + 5]))
        )) == 1:
            winner_found = True
            print 'Player ' + string[i] + ' won.'
            string[i - 1] = '$'
            string[i + 2] = '$'
            string[i + 5] = '$'
            break
        elif len(set(
            string[0] + string[4] + string[8]
        )) == 1:
            winner_found = True
            print 'Player ' + string[4] + ' won.'
            string[0] = '$'
            string[4] = '$'
            string[8] = '$'
            break
        elif len(set(
            string[2] + string[4] + string[6]
        )) == 1:
            winner_found = True
            print 'Player ' + string[4] + ' won.'
            string[2] = '$'
            string[4] = '$'
            string[6] = '$'
    if winner_found is not True:
        print 'There was a tie.'
    for i in range(1, 4):
        current = ''
        for char in string[(3 * i) - 3:3 * i]:
            current += char
        print current


for line in data:
    if line.count('=') == 9:
        break
    get_winner(line.rstrip())
