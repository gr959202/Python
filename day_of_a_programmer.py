#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    dict_noleap = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31 , '11':30, '12':31}
    dict_leap = {'01':31, '02':29, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
    if year%4  == 0:
        sum = 0
        for key in dict_leap:
            sum = sum + dict_leap[key]
            if sum >= 256:
                diff = sum - 256
                month = key
                day = dict_leap[key] - diff
                break
            else:
                continue
    else:
        sum = 0
        for key in dict_noleap:
            sum = sum + dict_noleap[key]
            if sum >= 256:
                diff = sum - 256
                month = key
                day = dict_noleap[key] - diff
                break
            else:
                continue
    day = str(day) + '.' + str(month) + '.' + str(int(year))
    return(day)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
