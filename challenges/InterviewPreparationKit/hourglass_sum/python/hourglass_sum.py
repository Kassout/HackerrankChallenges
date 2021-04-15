#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import compress


class MaskableList(list):
    def __getitem__(self, index):
        try:
            return super(MaskableList, self).__getitem__(index)
        except TypeError:
            return MaskableList(compress(self, index))


# Complete the hourglass_sum function below.
def hourglass_sum(arr):
    hourglass_number = len(arr[:-2]) * (len(arr[0]) - 2)
    pattern = [[True, True, True], [False, True, False], [True, True, True]]
    max = -math.inf
    for i in range(len(arr[:-2])):
        for j in range(len(arr[i]) - 2):
            hourglass = [x[j:j + 3] for x in arr[i:i + 3]]
            new = [MaskableList(sublist)[submask] for sublist, submask in zip(hourglass, pattern)]
            value = sum([sum(x) for x in new])
            if value > max:
                max = value
    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
