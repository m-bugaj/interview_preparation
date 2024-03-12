# TASK:

# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

# Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over all n days.

# Sample Input 0

# STDIN               Function
# -----               --------
# 9 5                 expenditure[] size n =9, d = 5
# 2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# Sample Output 0

# 2

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    if n < d:
        return
       
    #Optimal solution (with biscet):
    
    period = sorted(expenditure[:d])
    count = 0
    for i in range(d, n):
        if d % 2==0:
            medi = (period[d//2-1]+period[d//2])/2
        else:
            medi = period[d//2]
    
        if expenditure[i] >= medi*2:
            count += 1
    
        j = bisect.bisect(period, expenditure[i-d])
        period.pop(j-1)
        bisect.insort(period, expenditure[i])

    return count
    
    #Second solution:
    
    # count = 0
    # for i in range(0, n-d):
    #     median = statistics.median(expenditure[i:i+d])
    #     # print(median)
    #     # print(expenditure[i:i+d])
    #     if expenditure[i+d] >= median * 2:
    #         count += 1
            
    # return count

    
    #Third solution:
 
    # if d % 2 == 0:
    #     return sum(1 for i in range(0, n-d) if expenditure[i+d] >= sum(sorted(expenditure[i:i+d])[d//2-1:d//2+1]))
    # else:
    #     return sum(1 for i in range(0, n-d) if expenditure[i+d] >= 2 * sorted(expenditure[i:i+d])[d//2])
    
    #4th solution:
    
    # count = 0

    # for i in range(d, n):
    #     last_days = expenditure[i-d:i]
    #     last_days = sorted(last_days)
    #     # print(last_days)
    #     if d % 2 == 0:
    #         if expenditure[i] >= (last_days[d//2 + 1] + last_days[d//2]):
    #             count += 1
    #     else:
    #         if expenditure[i] >= (last_days[d//2]) * 2:
    #             count += 1

    # return count

if __name__ == '__main__':
    fptr = open('output/output_fraudulent_activity_notifications.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
