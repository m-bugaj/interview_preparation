# TASK:

# ABC is a right triangle, 90 degree  at B.
# Therefore, ABC = 90 degree .

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and BC.
# Your task is to find MBC (angle TETA, as shown in the figure) in degrees.

# SOLUTION:

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

degree_sign = u'\N{DEGREE SIGN}'

ab = int(input())
bc = int(input())
alfa = math.atan(ab/bc)

mc = math.sqrt(ab*ab+bc*bc) / 2
mb = math.sqrt(mc*mc+bc*bc-2*mc*bc*math.cos(alfa))
teta = math.acos((mc*mc-mb*mb-bc*bc)/(-2*mb*bc))

angle = teta * 180 / math.pi
    
print(str(round(angle)) + degree_sign)