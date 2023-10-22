# Write a Python program to find the first repeated character in a given string.

def first_repeated_char(s):
    x =set()
 
    for i in list(s):
        if i not in x:
            x.add(i)
        else:
            return i


if __name__ == "__main__":
    s = "abcdefdcdf"
    print(first_repeated_char(s))