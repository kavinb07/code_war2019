#!/usr/bin/python

from math import log10, ceil

# open data file
with open('parity_gap.txt', 'r') as f:
    data = f.readlines()


# Rounds number down to a nearest value. Accepts 2 parameters, num and place.
# num is the number to be rounded and place is the number to which num shall
# be rounded. num=23 and place=5 will round 23 down to the nearest multiple of
# 5, which is 20
def round_down(num, place):
    return int(float(num) / place) * place


# this function does the same as round_down, but num is rounded up to the
# nearest multiple of place
def round_up(num, place):
    return int(ceil(float(num) / place)) * place


# get_counts is the original function that would hang. it is used for small
# leftover values in this system
def get_counts(min, max):
    values = range(min, max + 1)
    even_parities = 0
    for value in values:
        binary = bin(value)[2:]
        ones = 0
        for char in binary:
            if char == '1':
                ones += 1
        if ones % 2 == 0:
            even_parities += 1
    return even_parities


def get_even_count(min, max):
    even_parities = 0
    max_log = int(log10(max))
    max_down = round_down(max, 10 ** max_log)

    if max_down > min:
        # first solve for the difference between max rounded down and max
        difference = max - max_down
        if max_down < max:
            new_max_log = int(log10(difference))
            # solve of the numbers between max rounded down and max
            while new_max_log > 0:
                parity_multiplier = round_down(
                    difference, 10 ** new_max_log
                ) / 10 ** new_max_log

                even_parities += (
                    parity_multiplier * (5 * (10 ** (new_max_log - 1)))
                )

                difference -= (
                    parity_multiplier * (10 ** new_max_log)
                )
                new_max_log -= 1
            even_parities += get_counts(0, difference)
        elif max_down == max:
            even_parities += get_counts(max, max)
        # now solve for min rounded to the same place as max and max
        min_up = round_up(min, 10 ** max_log)
        if min_up < max_down:
            difference = max_down - min_up
            new_max_log = int(log10(difference))

            parity_multiplier = round_down(
                difference, 10 ** new_max_log
            ) / 10 ** new_max_log

            even_parities += int(
                parity_multiplier * (5 * 10 ** (new_max_log - 1))
            )

        elif min_up == max_down:
            # there are no unsolved values between min_up and max_down, so the
            # program just passes
            pass
        # now solve for the values between min and min_up
        if min_up > min:
            new_max_log = int(log10(min_up))
            difference = min_up - min
            while new_max_log > 0:
                parity_multiplier = round_down(
                    difference, 10 ** new_max_log
                ) / 10 ** new_max_log
                even_parities += (
                    parity_multiplier * (5 * (10 ** (new_max_log - 1)))
                )
                difference -= (
                    parity_multiplier * (10 ** new_max_log)
                )
                new_max_log -= 1
            even_parities += get_counts(min, difference + min) - 1
    elif max_down < min and min != max:
        pass
    elif min == max:
        binary = bin(min)[2:]
        ones = 0
        for char in binary:
            if char == '1':
                ones += 1
        if ones % 2 == 0:
            even_parities += 1
    return even_parities


for line in data:
    values = line.split()
    val1 = int(values[0])
    val2 = int(values[1])
    if val1 == 0 and val2 == 0:
        break
    else:
        print get_even_count(val1, val2)
