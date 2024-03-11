# TASK:

# Consider the following version of Bubble Sort:

# for (int i = 0; i < n; i++) {
    
#     for (int j = 0; j < n - 1; j++) {
#         // Swap adjacent elements if they are in decreasing order
#         if (a[j] > a[j + 1]) {
#             swap(a[j], a[j + 1]);
#         }
#     }
    
# }
# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

# 1. Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
# 2. First Element: firstElement, where firstElement is the first element in the sorted array.
# 3. Last Element: lastElement, where lastElement is the last element in the sorted array.
# Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

# Sample Input 0

# STDIN   Function
# -----   --------
# 3       a[] size n = 3
# 1 2 3   a = [1, 2, 3]
# Sample Output 0

# Array is sorted in 0 swaps.
# First Element: 1
# Last Element: 3

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swaps = 0
    for _ in range(n):
        for i in range(n-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                swaps += 1
                
    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
