#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the counting_valleys function below.
def counting_valleys(steps, path):
    level = 0
    transition = 0
    for step in range(steps):
        if level == 0 and path[step] == 'D':
            transition += 1
        elif level == -1 and path[step] == 'U':
            transition += 1
        if path[step] == 'D':
            level -= 1
        elif path[step] == 'U':
            level += 1
    return math.floor(transition/2.0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = counting_valleys(steps, path)

    fptr.write(str(result))

    fptr.close()