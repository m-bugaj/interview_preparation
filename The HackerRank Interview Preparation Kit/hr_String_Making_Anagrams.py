# TASK:

# A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.

# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

# Sample Input

# cde
# abc
# Sample Output

# 4

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a2 = a
    b2 = b
    count = 0

    for i in range(len(a)):
        if a[i] in b2:
            b2 = b2.replace(a[i], "", 1)
        else:
            count += 1
            
    for i in range(len(b)):
        if b[i] in a2:
            a2 = a2.replace(b[i], "", 1)
        else:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open('output/output_strings_making_anagrams.txt', 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
