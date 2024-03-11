# TASK:

# Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

# 1.name: a string.
# 2.score: an integer.

# Sample Input

# 5
# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150
# Sample Output

# aleksa 150
# amy 100
# david 100
# aakansha 75
# heraldo 50

# SOLUTION:

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    # def __repr__(self):
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score == b.score:
            return 1 if a.name > b.name else -1
        else:
            return 1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)