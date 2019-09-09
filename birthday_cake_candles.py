#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    n = len(ar)
    ar.sort()
    mydict = {}
    for i in range(n):
        if ar[i] in mydict:
            mydict[ar[i]] += 1
        else:
            mydict[ar[i]] = 1
    my_list = []
    for key in mydict :
        my_list.append(mydict[key])
    
    last = my_list[-1]
    return last

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
