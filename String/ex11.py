#  Write a Python program to remove characters that have odd index values in a given string.
odd = lambda x: x % 2 != 0

def remove_char(s):
    res = " "
    for i in range(len(s)):
        if odd(i) == False:
            res = res + s[i]
    return res


if __name__ == "__main__":
    s = "python"
    print(remove_char(s))