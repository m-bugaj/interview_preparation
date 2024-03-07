# TASK:

# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# Sample Input

# 2
# hello
# world
# hi
# world
# Sample Output

# YES
# NO

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    d1 = list(dict.fromkeys(list(s1)))
    d2 = list(dict.fromkeys(list(s2)))
    
    for i in range(len(d1)):
        if d1[i] in d2:
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open('output/output_two_strings.txt', 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
