# TASK: 
# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

# Example
# s = mom

# The list of all anagrammatic pairs is [m,m], [mo,om] at positions [[0],[2]], [[0,1],[1,2]] respectively.

# Function Description

# Complete the function sherlockAndAnagrams in the editor below.

# sherlockAndAnagrams has the following parameter(s):

# string s: a string
# Returns

# int: the number of unordered anagrammatic pairs of substrings in 
# Input Format

# The first line contains an integer , the number of queries.
# Each of the next  lines contains a string  to analyze.

# Constraints



#  contains only lowercase letters in the range ascii[a-z].

# Sample Input 0

# 2
# abba
# abcd
# Sample Output 0

# 4
# 0

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    ss_dict = {}
    anagrams = 0

    for length in range(1, len(s)):
        for i in range(len(s) - length + 1):
            sorted_ss = ''.join(sorted(s[i:i+length]))
            if sorted_ss in ss_dict.keys():
                ss_dict[sorted_ss] += 1
            else:
                ss_dict[sorted_ss] = 0
            if ss_dict[sorted_ss] > 0:
                anagrams += ss_dict[sorted_ss]
    
    return anagrams

if __name__ == '__main__':
    fptr = open('output/output_sherlock_and_anagrams.txt', 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
