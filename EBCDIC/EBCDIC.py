#!/usr/bin/python

with open('EBCDIC.txt') as f:
    data = f.readlines()


convert = {'81': 'a', '82': 'b', '83': 'c', '84': 'd', '85': 'e', '86': 'f',
           '87': 'g', '88': 'h', '89': 'i', '91': 'j', '92': 'k', '93': 'l',
           '94': 'm', '95': 'n', '96': 'o', '97': 'p', '98': 'q', '99': 'r',
           'A2': 's', 'A3': 't', 'A4': 'u', 'A5': 'v', 'A6': 'w', 'A7': 'x',
           'A8': 'y', 'A9': 'z', 'C1': 'A', 'C2': 'B', 'C3': 'C', 'C4': 'D',
           'C5': 'E', 'C6': 'F', 'C7': 'G', 'C8': 'H', 'C9': 'I', 'D1': 'J',
           'D2': 'K', 'D3': 'L', 'D4': 'M', 'D5': 'N', 'D6': 'O', 'D7': 'P',
           'D8': 'Q', 'D9': 'R', 'E2': 'S', 'E3': 'T', 'E4': 'U', 'E5': 'V',
           'E6': 'W', 'E7': 'X', 'E8': 'Y', 'E9': 'Z', '40': ' ', '4B': '.',
           '6B': ',', '5A': '!'}


for i in range(1, len(data)):
    string = ''
    for j in range(1, len(data[i].split())):
        string += convert[data[i].split()[j]]
    print(string)
