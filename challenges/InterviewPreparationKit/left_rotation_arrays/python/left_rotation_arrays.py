#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the left_rotation_arrays function below.
def left_rotation_arrays(a, d):
    movement = d % len(a)
    a = [a[(i+d) % n] for i in range(n)]
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = left_rotation_arrays(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()