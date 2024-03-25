# TASK:

# You will be given a list of integers, arr, and a single integer k. You must create an array of length k from elements of arr such that its unfairness is minimized. Call that array arr'. Unfairness of an array is calculated as
# max(arr')-min(arr')

# Sample Input 0

# 7
# 3
# 10
# 100
# 300
# 200
# 1000
# 20
# 30
# Sample Output 0

# 20
# Explanation 0

# Here k=3; selecting the 3 integers 10,20,30, unfairness equals

# max(10,20,30) - min(10,20,30) = 30 - 10 = 20

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    unfairness = arr[k-1] - arr[0]

    for i in range(0, n-k+1):
        temp = arr[i+k-1] - arr[i]
        if temp < unfairness:
            unfairness = temp
    
    return unfairness

if __name__ == '__main__':
    fptr = open('output/output_max_min.txt', 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
