# TASK:

# The absolute difference is the positive difference between two values a and b, is written |a-b| or |b-a| and they are equal. If a=3 and b=2, |3-2|=|2-3|=1. Given an array of integers, find the minimum absolute difference between any two elements in the array.

# Sample Input 0

# 3
# 3 -7 0
# Sample Output 0

# 3

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    return min(arr[i+1] - arr[i] for i in range(n-1))

if __name__ == '__main__':
    fptr = open('output/output_minimum_absolute_difference_in_an_array.txt', 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
