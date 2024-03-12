# TASK:

# In an array, arr, the elements at indices i and j (where i<j) form an inversion if arr[i]>arr[j]. In other words, inverted elements arr[i] and arr[j] are considered to be "out of order". To correct an inversion, we can swap adjacent elements.

# Sample Input

# STDIN       Function
# -----       --------
# 2           d = 2
# 5           arr[] size n = 5 for the first dataset
# 1 1 1 2 2   arr = [1, 1, 1, 2, 2]
# 5           arr[] size n = 5 for the second dataset     
# 2 1 3 1 2   arr = [2, 1, 3, 1, 2]
# Sample Output

# 0  
# 4   

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Optimal solution:

N_swaps = 0
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    med = n//2
    sub1 = merge_sort(arr[:med])
    sub2 = merge_sort(arr[med:])

    global N_swaps

    sorted_arr = []
    i, j = 0, 0
    while i < len(sub1) and j < len(sub2):
        if sub1[i] <= sub2[j]:
            sorted_arr.append(sub1[i])
            i += 1
        elif sub1[i] > sub2[j]:
            sorted_arr.append(sub2[j])
            j += 1
            
            N_swaps += len(sub1) - i
    if i < len(sub1):
        sorted_arr += sub1[i:]
        
    if j < len(sub2):
        sorted_arr += sub2[j:]
    return sorted_arr

def countInversions(arr):
    # Write your code here
    global N_swaps
    N_swaps = 0
    merge_sort(arr)
    return N_swaps
    
    # Solution 2:
    
    # count = 0
    # for j in range(n):
    #     count += sum(1 for i in range(j, n-1) if arr[j] > arr[i+1])
    #     print(count)
        
    # return count

    # Solution 3:
    
    
    # swap = False
    # count = 0
    # sorted_arr = sorted(arr)
    
    # while arr != sorted_arr:
    #     for i in range(n-1):
    #         if arr[i] <= arr[i+1]:
    #             continue
    #         else:
    #             swap = True
                
    #         j = i
    #         while swap is True:
    #             temp = arr[j]
    #             arr[j] = arr[j+1]
    #             arr[j+1] = temp
    #             count += 1
    #             if arr[j+1] >= arr[j]:
    #                 swap = False
    #         # print(arr)
                
    # return count
    
    # Solution 4 but
    # bad answer:
    
    # count = 0
    
    # while True:
    #     max_int = max(arr[:n-1])
    #     max_int_index = arr.index(max_int, 0, n-1)
    #     min_int = min(arr[max_int_index:])
    #     min_int_index = arr.index(min_int, max_int_index)
    #     print()
    #     print(max_int, max_int_index, min_int, min_int_index)
    #     print(arr)
    #     if max_int_index < min_int_index and max_int > min_int:
    #         arr[min_int_index] = max_int
    #         arr[max_int_index] = min_int
    #         count += 1
    #     else:
    #         return count

if __name__ == '__main__':
    fptr = open('output/output_merge_sort_counting_inversions.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
