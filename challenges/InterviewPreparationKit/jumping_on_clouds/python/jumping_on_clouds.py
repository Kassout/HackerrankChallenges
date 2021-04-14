#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumping_on_clouds function below.
def jumping_on_clouds(c):
    jumps = 0
    i = 0
    while i < len(c)-1:
        if i+2 < len(c) and (c[i] == 0 and c[i+2] == 0):
            jumps += 1
            i += 1
        else:
            jumps += 1
        i += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    fptr.write(str(result))

    fptr.close()