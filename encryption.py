#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(" ","")
    sq_rt = math.sqrt(len(s))
    min = math.floor(sq_rt)
    max = math.ceil(sq_rt)
    sq_lis = []
    s_copy = ""
    for i in range(min):
        s_copy = s_copy + s[i*max:(i+1)*max]
        if s == s_copy:
            print("We have printed the entire string")
            sq_lis.append(str(s[i*max:(i+1)*max]))
        else:
            sq_lis.append(str(s[i*max:(i+1)*max]))
    return(sq_lis)
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()
