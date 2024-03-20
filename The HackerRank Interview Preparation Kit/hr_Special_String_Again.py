# TASK:
# A string is said to be a special string if either of two conditions is met:

# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
# A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.

# Example
# s = mnonopoo

#  contains the following 12 special substrings: m, n, o, n, o, p, o, o, non, ono, opo, oo.

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    m = 0
    
    for i in range(n):
        count += 1
        j = i
        
        if i < n - 1:
            if s[i] == s[i+1]:
                while s[j+1] == s[i]:
                    count += 1
                    # if j < n - 2:
                    j += 1
                    if j == n - 1:
                        break

        if i < n - 2:
            if s[i] != s[i+1] and s[i] == s[i+2]:
                while s[j+2] == s[i] and s[i-m] == s[i]:
                    count += 1
                    j += 1
                    if j == n - 2:
                        break
                    m += 1

        m = 0
        
    return count


if __name__ == '__main__':
    fptr = open('output/output_special_string_again.txt', 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
