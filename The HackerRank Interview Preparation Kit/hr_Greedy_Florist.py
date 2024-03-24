# TASK:

# A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1. The first flower will be original price, (0+1) x original price, the next will be (1+1) x original price and so on.

# Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, determine the minimum cost to purchase all of the flowers. The number of flowers they want equals the length of the c array.

# Function Description

# Complete the getMinimumCost function in the editor below.

# getMinimumCost has the following parameter(s):

# int c[n]: the original price of each flower
# int k: the number of friends
# Returns
# - int: the minimum cost to purchase all flowers

# Sample Input 2

# 5 3
# 1 3 5 7 9
# Sample Output 2

# 29

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    cp = 1
    total_cost = 0
    
    for i in range(n):
        total_cost += cp * c[i]
        if (i+1) % k == 0:
            cp += 1
            
    return total_cost
        

if __name__ == '__main__':
    fptr = open('output/output_greedy_florist.txt', 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
