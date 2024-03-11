# TASK:

# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

# OPIS ALGORYTMU PL:
# W tym zadaniu optymalnym podejściem jest zastosowanie algorytmu który zapewnia, że nie zamienimy dwukrotnie miejscami aktualnie branej pod uwagę liczby.
# Na początku potrzebna jest tablica zmiennych typu bool aby zaznaczać na true miejsca z których wzięto liczbę i ją przestawiono.
# Jeżeli algorytm napotka miejsce, które jest poprawne lub zostało już wykorzystane do zamiany to przechodzi do następnej iteracji.
# Jeżeli algorytm napotka niewałaściwe miejsce to zlicza miejsca, które nie są na właściwym miejscu, aż napotka na miejsce które zostało zamienione jako pierwsze w danym cyklu.
# Następnie while przerywa działanie i zliczają się cykle z odjęciem tego ostatniego, ponieważ tam zaszła już zamiana w pierwszym cyklu.

# Sample Input 0

# 4
# 4 3 1 2
# Sample Output 0

# 3

# SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # count = 0
    # sorted_arr = sorted(arr)
    # for i in range(n):
    #     if arr[i] == i + 1:
    #         if sorted_arr[i:] == arr[i:]:
    #             return count
    #         continue
        
    #     if i + 1 in arr[i+1:]:
    #         arr[arr.index(i + 1, i + 1)] = arr[i]
    #         count += 1
        

    # return count

    #OPTIMAL SOLUTION:
    
    count = 0
    visited = [False] * len(arr)
    for i in range(len(arr)):
        if visited[i] or arr[i] == i + 1:
            continue

        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arr[j] - 1
            cycle_size += 1

        count += cycle_size - 1

    return count

if __name__ == '__main__':
    fptr = open('output/output_minimum_swaps_2.txt', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
