from ex42 import repeated_char
# Write a Python program to find the first repeated character in a given string.

first_repeated_char = lambda s: list(repeated_char(s).keys())[0]


if __name__ == "__main__":
    s = "abcdefcdf"
    print(first_repeated_char(s))