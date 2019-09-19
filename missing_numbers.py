#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    a_ele = {}
    b_ele = {}
    for items in arr:
        if items not in a_ele:
                a_ele[items] = 1
        else:
                a_ele[items] += 1


    for items in brr:
        if items not in b_ele:
                b_ele[items] = 1
        else:
                b_ele[items] += 1

    list_diff = []
    seen = set()
    for key in b_ele:
        if key in a_ele and b_ele[key] == a_ele[key]:
                continue
        elif key in a_ele and b_ele[key] != a_ele[key]:
                list_diff.append(key)
        else:
                list_diff.append(key)

    list_diff.sort()
    return list_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
