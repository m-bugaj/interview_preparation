def is_scrambled_palindrome(s):
    check_list = []
    s_len = len(s)
    for x in s:
        if s.count(x) % 2 == 0:
            check_list.append(True)
            s = s.replace(x, '')
        else:
            check_list.append(False)
            s = s.replace(x, '')
        if len(s) == 0:
            break

    if s_len % 2 == 0 and check_list.count(False) == 0:
        print("True")
    elif s_len % 2 != 0 and check_list.count(False) == 1:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    s = input().strip()
    is_scrambled_palindrome(s)