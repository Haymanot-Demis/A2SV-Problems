#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    indx = n - 2
    last_num = arr[-1]
    while indx >= 0  and arr[indx] > last_num:
        arr[indx + 1] = arr[indx]
        indx -= 1
        print(*arr)
    arr[indx + 1] = last_num
    print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
