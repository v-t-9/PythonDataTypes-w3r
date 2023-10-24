# Write a Python program to count the number of substrings with the same first and last characters in a given string.

def first_last_same_char(s):
    l = s.split()
    c = 0
    for i in l:
        if i[0] == i[-1]:
            c = c + 1
    
    return c


if __name__ == "__main__":
    s = "aba abc bab bcd cbc acd"
    print(first_last_same_char(s))