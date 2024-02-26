# TASK:
# One of the built-in functions of Python is divmod, which takes two arguments  and  and returns a tuple containing the quotient of  first and then the remainder .

# For example:

# >>> print divmod(177,10)
# (17, 7)
# Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

# Task
# Read in two integers,  and , and print three lines.
# The first line is the integer division  (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: .
# The third line prints the divmod of  and .

# SOLUTION:

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    dm = divmod(x,y)
    print(dm[0])
    print(dm[1])
    print(dm)