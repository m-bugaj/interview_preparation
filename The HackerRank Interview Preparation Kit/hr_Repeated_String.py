# TASK: 
# There is a string, s , of lowercase English letters that is repeated infinitely many times. Given an integer, n , find and print the number of letter a's in the first n letters of the infinite string.

# Example
# s='abcac'
# n=10

# The substring we consider is abcacabcac, the first  characters of the infinite string. There are 4 occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Returns

# int: the frequency of a in the substring

# Sample Input

# Sample Input 0

# aba
# 10
# Sample Output 0

# 7

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    a_in_s = s.count('a')
    count_of_a = (n // len(s)) * a_in_s
    rest_of_a = [s[i % len(s)] for i in range(n % len(s))].count('a')
    return count_of_a + rest_of_a

if __name__ == '__main__':
    fptr = open('output/output_repeated_string.txt', 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
