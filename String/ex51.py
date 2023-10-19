from ex42 import repeated_char
# Write a Python program to find the first non-repeating character in a given string.

def first_nonrepeating_char(s):
    res = []
    for i in s:
        if i not in repeated_char(s).keys():
            res.append(i)
    
    return res[0]


if __name__ == "__main__":
    s = "apple pear orange"
    print(first_nonrepeating_char(s))