# Write a Python program to count the number of non-empty substrings of a given string.

non_empty_substr = lambda s: int((len(s)) * (len(s) + 1) / 2)


if __name__ == "__main__":
    s = "Python"
    print(non_empty_substr(s))