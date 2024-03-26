# TASK:

# Given a string s such that s = merge(reverse(A), shuffle(A)) for some string A, find the lexicographically smallest A.

# For example, s=abab. We can split it into two strings of ab. The reverse is ba and we need to find a string to shuffle in to get abab. The middle two characters match our reverse string, leaving the a and b at the ends. Our shuffle string needs to be ab. Lexicographically ab<ba, so our answer is ab.

# Sample Input 1

# abcdefgabcdefg
# Sample Output 1

# agfedcb

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    # Write your code here
    # find character frequencies in the desired string A
    freq = {key: val // 2 for key, val in Counter(s).items()}

    # repeat gready approach until solution is complete
    solution = []
    n = len(s)
    while len(solution) < n // 2:
        left_freq = Counter(s)
        next_char = {}
        min_char = '~'
        # search original string S backwards
        for index in range(len(s)-1, -1, -1):
            char = s[index]
            # it is possible to take this char as the next one
            if char not in next_char and freq[char] > 0:
                next_char[char] = index
                min_char = min(min_char, char)
            # there's not enough letters available to the left
            left_freq[char] -= 1
            if left_freq[char] < freq[char]:
                break
        # add minimal char as the next one (greedy)
        solution += min_char
        freq[min_char] -= 1
        s = s[0:next_char[min_char]]

    return "".join(solution)

if __name__ == '__main__':
    fptr = open('output/output_reverse_shuffle_merge.txt', 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
