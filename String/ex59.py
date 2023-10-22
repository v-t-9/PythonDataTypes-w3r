
from ex2 import num_char
# Write a Python program to find the maximum number of characters in a given string.

def max_num_char(s):
    d = num_char(s)
    ma = max(list(d.values()))
    for i in d:
        if d[i] == ma:
            return { i : d[i] }

if __name__ == "__main__":
    s = "aaabbbcdddeeaabbabb"
    print(max_num_char(s))