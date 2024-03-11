#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    # arr = [0] * n
    # index = []
    # for i in range(len(queries)):
    #     index.append(queries[i][0])
    #     index.append(queries[i][1])
    # min_index = min(index)
    # max_index = max(index)

    # for i in range(len(queries)):
    #     for j in range(queries[i][0] - 1, queries[i][1]):
    #         arr[j] += queries[i][2]

    # return max(arr)

    #OPTIMAL SOLUTION:
    
    arr = [0] * n
    
    for query in queries:
        arr[query[0] - 1] += query[2]
        if query[1] < n:
            arr[query[1]] -= query[2]

    value = 0
    max_value = 0
    for x in arr:
        value += x
        max_value = max(max_value, value)
    
    return max_value

if __name__ == '__main__':
    fptr = open('output/output_array_manipulation.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
