# Write a Python program to remove all characters except a specified character from a given string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:
# P
# Original string
# google
# Remove all characters except g in the said string:
# gg
# Original string
# exercises
# Remove all characters except e in the said string:
# eee

def remove_chars(s,c):
    res = ""
    for i in s:
        if i != c:
            continue
        else:
            res = res + i
    return res
if __name__ == "__main__":
    s1 = "Python Exercises"
    c1 = "P"
    s2 = "google"
    c2 = "g"
    s3 = "exercises"
    c3 = "e"
    print(remove_chars(s1,c1))
    print(remove_chars(s2,c2))
    print(remove_chars(s3,c3))