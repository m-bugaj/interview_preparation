# TASK:

# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

# Given the value of money and the cost of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a cost. For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.
    
# Sample Input

# STDIN       Function
# -----       --------
# 2           t = 2
# 4           money = 4
# 5           cost[] size n = 5
# 1 4 5 3 2   cost = [1, 4, 5, 3, 2]
# 4           money = 4
# 4           cost[] size n = 4
# 2 2 4 3     cost = [2, 2, 4, 3]
# Sample Output

# 1 4
# 1 2

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    # Optimal Solution:
    index_dict = {}
    for index, value in enumerate(cost):
        index_dict[value] = index
        # print(index_dict)

    for i, c in enumerate(cost):
        diff = money - c
    
        if diff in index_dict and index_dict[diff] > i:
            print(i+1, index_dict[diff]+1)
            break
    
    # Solution 2
    # for i in range(n):
    #     if money - cost[i] in cost[i:] and cost[i] in cost[i:] and money - cost[i] in cost[i+1:]:
    #         i_1 = cost.index(cost[i], i) + 1
    #         i_2 = cost.index(money - cost[i], i+1) + 1
    #         print(i_1, i_2)
    #         break

    # Solution 3
    # s_cost = sorted(cost)
    # for i in range(n):
    #     cost_1 = s_cost[i]
    #     cost_2 = money - s_cost[i]
    #     f_i = s_cost.index(cost_1, i) + 1
    #     if cost_2 in s_cost[f_i:]:
    #         first_index = cost.index(cost_1) + 1
    #         if cost_2 in cost[first_index:]:
    #             second_index = cost.index(cost_2, first_index) + 1
    #             print(first_index, second_index)
    #         elif cost_2 in cost[:first_index-1]:
    #             second_index = cost.index(cost_2, 0, first_index-1) + 1
    #             print(second_index, first_index)
    #     elif s_cost[i] >= money:
    #         break

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
