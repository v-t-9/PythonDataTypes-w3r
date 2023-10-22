# Write a Python program to capitalize the first and last letters of each word in a given string.

capitalize_first_last = lambda s: s[0].upper() + s[1:len(s)-1] + s[-1].upper()
if __name__ == "__main__":
    s = "abcdefg"
    print(capitalize_first_last(s))