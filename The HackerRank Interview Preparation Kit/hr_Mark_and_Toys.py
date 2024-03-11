# TASK:

# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

# Note Each toy can be purchased only once.

# Example
# prices=[1,2,3,4]
# k=7

# The budget is 7 units of currency. He can buy items that cost [1,2,3] for 6, or [3,4] for 7 units. The maximum is 3 items.

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    spend = 0
    count = 0
    for price in prices:
        if spend < k and price + spend <= k:
            spend += price
            count += 1
        else:
            return count

if __name__ == '__main__':
    fptr = open('output/output_mark_and_toys.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
