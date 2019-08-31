## Problems of apples and oranges 
##https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=profile

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_app = 0
    count_org = 0
    n_app = len(apples)
    n_org = len(oranges)
    for i in range(n_app):
        dist_a = 0
        dist_a = apples[i] + a
        if dist_a < s or dist_a > t:
            continue
        else:
            count_app  = count_app + 1

    for i in range(n_org):
        dist_o = 0
        dist_o = oranges[i] + b
        if dist_o > t or dist_o < s:
            continue    
        else:
            count_org = count_org + 1
    print(count_app)
    print(count_org)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
