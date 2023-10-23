# Write a Python program to remove all consecutive duplicates of a given string.
def remove_consecutive_duplicates(s):
    a = 0
    b = 0
    res = " "
    while a < len(s):
        
        if s[a] == s[b]:
            a = a +1
        elif s[a] != s[b]:
            res = res + s[b]
            b = a
            a = a + 1

    res = res + s[a-1]
    return res
if __name__ == "__main__":
    s = "aababb"
    print(remove_consecutive_duplicates(s))

