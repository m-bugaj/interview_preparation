# TASK:

# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other string. Letters cannot be rearranged. Given two strings of equal length, what's the longest string that can be constructed such that it is a child of both?

# Example
# s1 = 'ABCD'
# s2 = 'ABDC'


# These strings have two children with maximum length 3, ABC and ABD. They can be formed by eliminating either the D or C from both strings. Return 3.

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    n=len(s1)
    s1='0'+s1
    s2='1'+s2
    count=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s1[i]==s2[j]:
                count[i][j]=count[i-1][j-1]+1
            else:
                count[i][j]=max(count[i-1][j], count[i][j-1])
    return count[n][n]
        

if __name__ == '__main__':
    fptr = open('output/output_common_child.txt', 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
