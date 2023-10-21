from ex53 import first_repeated_char
# Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.

if __name__ == "__main__":
    s = "abbcbc"
    print(s.find(first_repeated_char(s)))