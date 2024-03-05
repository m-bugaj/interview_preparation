# TASK:
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
# SOLUTION:

# Enter your code here. Read input from STDIN. Print output to STDOUT

height, width = input().split(" ")
w = int(width)
h = int(height)

pattern = ""
s = ".|."

#TOP
for i in range((h-1)//2):
    s_in_line = ".|." + 2 * (s * (i))
    pattern += s_in_line.center(w, "-") + "\n"

#CENTER
pattern += "WELCOME".center(w, "-") + "\n"

#BOTTOM
for i in range(((h-1)//2)-1, -1, -1):
    s_in_line = ".|." + 2 * (s * i)
    pattern += s_in_line.center(w, "-") + "\n"
print(pattern.strip())