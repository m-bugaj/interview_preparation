# TASK:

# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

# Sample Input 1

# aabbccddeefghi
# Sample Output 1

# NO
# Explanation 1

# Frequency counts for the letters are as follows:

# {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

# Sample Input 2

# abcdefghhgfedecba
# Sample Output 2

# YES
# Explanation 2

# All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    
    characters = {}
    isOneDouble = False
    
    for x in s:
        characters[x] = characters.get(x, 0) + 1
    
    for k in characters:
        if characters[s[0]] != characters[k] and isOneDouble:
            return "NO"
        elif characters[s[0]] != characters[k]:
            isOneDouble = True
            
    return "YES"
    

if __name__ == '__main__':
    fptr = open('output/output_sherlock_and_the_valid_string.txt', 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
