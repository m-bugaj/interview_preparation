# TASK:
# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

# Example
# magazine = "attack at dawn" note = "Attack at dawn"

# The magazine has all the right words, but there is a case mismatch. The answer is No.

# Function Description

# Complete the checkMagazine function in the editor below. It must print Yes if the note can be formed using the magazine, or No.

# checkMagazine has the following parameters:

# string magazine[m]: the words in the magazine
# string note[n]: the words in the ransom note
# Prints

# string: either Yes or No, no return value is 

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    m_dict = {}
    for i in range(m):
        if magazine[i] in m_dict.keys():
            m_dict[magazine[i]] += 1
        else:
            m_dict[magazine[i]] = 1
        
    for i in range(n):
        if note[i] in m_dict.keys():
            if m_dict[note[i]] > 0:
                m_dict[note[i]] -= 1
            else:
                print("No")
                return
        else:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
