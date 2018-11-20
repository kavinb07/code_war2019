#!/usr/bin/python

from math import log, ceil

#Basic assumption is for 5 bits binary max value it can have is
## 0b11111 (32 decimal). The number of evens is 32/2 = 16
## If the number of bits is 6 max number if 64 an number of evens is 32
## Number of evens is half of max value

## Once the number of evens for the max value is found, the difference
## use the normal method to calculate by spliting the character arrays
def get_even_counts(min, max):
    even_parities = 0
    for value in range(long(min), long(max)):
        binary = bin(value)[2:]
        ones = 0
        for char in binary:
            if char == '1':
                ones += 1
        if ones % 2 == 0:
            even_parities += 1
    return even_parities

##Number of binary digits used by a number is found using the log(value,2)
##which is log base 2. For  log(20,2) will give integer 4. Max value for
## 4 digit binary is 16. Number of evens is 16/2 = 8. Difference 20 - 16
## find the even using normal methods
def cal_even_parity(val) :
    max_digits = float(log(val,2))
    max_value  = 2 ** max_digits

    num_even = long(max_value/2)
    return num_even + get_even_counts(max_value+1,val)

# open data file
with open('parity_gap_bala.txt', 'r') as f:
    data = f.readlines()

for line in data:
    values = line.split()
    val1 = int(values[0])
    val2 = int(values[1])
    if val1 == 0 and val2 == 0:
        break
    else:
       if val1 == 0 :
          #print " start to calculate parity for " + str(val1) + " " + str(val2)
          print str(cal_even_parity(val2))
       else :
          #print " start to calculate parity for " + str(val1) + " " + str(val1)
          num_even = cal_even_parity(val2) - cal_even_parity(val1-1)
          print str(num_even)
