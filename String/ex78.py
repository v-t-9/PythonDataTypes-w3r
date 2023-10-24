#  Write a Python program to count characters at the same position in a given string (lower and uppercase characters) as in the English alphabet.

def same_position_alphabet(s):
    res = 0
    for i in range(len(s)):
        if ord(s[i]) - ord("A") == i or ord(s[i]) - ord("a") == i:
            res = res + 1
    return res


if __name__ == "__main__":
    s = "awzref"
    
    print(same_position_alphabet(s))