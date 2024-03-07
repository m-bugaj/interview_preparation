# TASK:
# There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

# For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

# Sample Input 0

# 7
# 0 0 1 0 0 1 0
# Sample Output 0

# 4

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    double_jump = False
        
    for i in range(n-1):
        if c[i] == 0 and c[i+1] == 0 and not double_jump:
            jumps += 1
            if i < n-2:
                if c[i+2] == 0:
                    double_jump = True
        elif double_jump:
            double_jump = False
        if c[i] == 0 and c[i+1] == 1:
            jumps += 1
    
    return jumps

if __name__ == '__main__':
    fptr = open('output/output_Jumping_on_the_Clouds.txt', 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
