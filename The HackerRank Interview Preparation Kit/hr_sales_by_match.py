# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

# Example
# n = 7
# ar = [1,2,1,2,1,3,2]

# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

# Function Description

# Complete the sockMerchant function in the editor below.

# sockMerchant has the following parameter(s):

# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns

# int: the number of pairs

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    result_dict = {}
    for i in ar:
        result_dict[i] = ar.count(i)
        
    return int(sum(value / 2 if value % 2 == 0 else (value - 1) / 2 for key, value in result_dict.items()))


if __name__ == '__main__':
    fptr = open('output/output_sales_by_match.txt', 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
