# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# SOLUTION:

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)