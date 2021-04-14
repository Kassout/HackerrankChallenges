#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sales_by_match function below.
def sales_by_match(n, ar):
    match_count = 0
    values = set(ar)
    for x in values:
        matches = [value for value in ar if value == x]
        match_count += math.floor(len(matches)/2.0)
    return match_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sales_by_match(n, ar)

    fptr.write(str(result))

    fptr.close()