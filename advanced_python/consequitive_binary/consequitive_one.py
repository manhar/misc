#!/user/bin/python

# !/bin/python3

import math
import os
import random
import re
import sys

"""
Task: for a given base-10 interger n, convert to binary (based-2) and print the maximum number of consecutive 1s 

base-10 input: 5
binary: 101
cosecutive 1's: 1 

base-10 input: 13 
binary: 1101
consecutive 1: 2  

6/2 = 3  remainder 0
3/2 = 1 remainder 1 
110 

5/2 = 2 remainder 1 
2/2 = 1 remainder 0
101

7/2 = 3 remainder 1 
3/2 = 1 remainder 1
111 

8/2 = 4 remainder 0
4/2 = 2 remainder 0
2/2 = 1 remainder 0
1000

3/2 = 1 remainder 1 
11

2/2 = 1 remainder 0

1/2 = 0.5 remainder 1



"""


def binary(n):
    l = []
    while n > 0:
        remainder = n % 2
        pre_val = n
       # print("pre =>", n, "remainder=>", remainder)
        n = int(n / 2)

        l.append(remainder)
        if n == 1:
            l.append(1)
            break

       # print("post ", pre_val, "/2 =", n, "remainder=>",remainder)

        #print(l)

    l.reverse()
    return ("".join([str(i) for i in l ]))


def consecutive_one(n):
    l = binary(n)
    result = []
    print(l)
    counter = 0
    for i in l:
        # print(i)
        if "1" == i:
            counter += 1
            result.append(counter)
        else:
            counter = 0
            result.append(counter)

    return (max(result))


if __name__ == '__main__':
    print("Input:")
    n = int(input())
    print(consecutive_one(n))

