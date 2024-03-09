# TASK:

# You are given  queries. Each query is of the form two integers described below:
# - 1 x : Insert x in your data structure.
# - 2 y : Delete one occurence of y from your data structure, if present.
# - 3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

# The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1] contains the data element.

# Example
# queries=[(1,1),(2,2),(3,2),(1,1),(2,1),(3,2)]
# The results of each operation are:

# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# Return an array with the output: [0,1].

# Function Description

# Complete the freqQuery function in the editor below.

# freqQuery has the following parameter(s):

# int queries[q][2]: a 2-d array of integers
# Returns
# - int[]: the results of queries of type 3

# Sample Input 0

# 8
# 1 5
# 1 6
# 3 2
# 1 10
# 1 10
# 1 6
# 2 5
# 3 2
# Sample Output 0

# 0
# 1

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    my_dict = {}
    result = []
    for query in queries:
        if query[0] == 1:
            my_dict[query[1]] = my_dict.get(query[1], 0) + 1
        if query[0] == 2 and query[1] in my_dict.keys():
            if my_dict[query[1]] > 0:
                my_dict[query[1]] -= 1
        if query[0] == 3 and query[1] in my_dict.values():
            result.append(1)
        elif query[0] == 3:
            result.append(0)

    return result

if __name__ == '__main__':
    fptr = open('output/output_frequency_queries.txt', 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
