#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    min_loss = 1000000000
    length = len(price)
    for i in range(length):
        for j in range(i+1,length):
            if price[i] == price[j]:
                continue
            else:
                loss = price[i] - price[j]
            if loss > 0 and loss < min_loss:
                min_loss = loss
            
    return min_loss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
