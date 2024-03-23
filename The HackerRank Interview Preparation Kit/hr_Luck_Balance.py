# TASK:
# Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, L[i] and T[i]:

# L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i].
# T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
# If Lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.

# Sample Input

# STDIN       Function
# -----       --------
# 6 3         n = 6, k = 3
# 5 1         contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
# 2 1
# 1 1
# 8 1
# 10 0
# 5 0
# Sample Output

# 29

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    luck = 0
    important_contests = []
    heapq.heapify(important_contests)
    
    for i in range(len(contests)):
        if contests[i][1] == 0:
            luck += contests[i][0]   
        if contests[i][1] == 1:
            heapq.heappush(important_contests, contests[i][0])
            
    for _ in range(len(important_contests) - k): 
        luck -= heapq.heappop(important_contests)

    return sum(important_contests) + luck

if __name__ == '__main__':
    fptr = open('output/output_luck_balance.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
