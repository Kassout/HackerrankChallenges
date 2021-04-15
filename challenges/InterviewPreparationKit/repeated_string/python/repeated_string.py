#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeated_string function below.
def repeated_string(s, n):
    a_count = s.count('a')
    s_number = math.floor(n/len(s))
    a_total = s_number * a_count
    if s_number == 0:
        s_rest = n
    else:
        s_rest = n % s_number
    a_total += s.count('a', 0, s_rest)
    return a_total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()