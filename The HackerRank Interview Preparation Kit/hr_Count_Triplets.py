# TASK:
# You are given an array and you need to find number of tripets of indices (I,J,K) such that the elements at those indices are in geometric progression for a given common ratio r and i<j<k.

# Example

# arr=[1,4,16,64] r=4

# There are [1,4,16] and [4,16,64] at indices (0,1,2) and (1,2,3). Return 2.

# Function Description

# Complete the countTriplets function in the editor below.

# countTriplets has the following parameter(s):

# int arr[n]: an array of integers
# int r: the common ratio
# Returns

# int: the number of triplets

# Sample Input 0

# 4 2
# 1 2 2 4
# Sample Output 0

# 2
# Explanation 0

# There are 2 triplets in satisfying our criteria, whose indices are (0,1,3) and (0,2,3)

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    potential_pairs = {}
    potential_singles = {}

    for k in arr:
        if k in potential_pairs:
            count += potential_pairs[k]

        if k in potential_singles:
            potential_pairs[k * r] = potential_pairs.get(k * r, 0) + potential_singles[k]

        potential_singles[k * r] = potential_singles.get(k * r, 0) + 1

    return count
    
    # non optimal solution
    # t_dict = {}
    # for x in range(n):
    #     for length in range(2, n - x):
    #         i = arr[x]
    #         j = arr[length-1+x]
    #         if i * r == j:
    #             k = j*r
    #             k_count = arr[length+x:len(arr)].count(k)
    #             key = str([i, j, k])
    #             if key in t_dict.keys():
    #                 t_dict[key] += k_count
    #             else:
    #                 t_dict[key] = k_count
    #             print(key) 
    # return sum(t_dict.values())

if __name__ == '__main__':
    fptr = open('output/output_count_triplets.txt', 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
