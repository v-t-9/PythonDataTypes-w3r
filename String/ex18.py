# Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

def first_three(s):
    if len(s)>=3:
        return s[:3]
    else:
        return s


if __name__ == "__main__":
    s1 = "ipy"
    s2 = "python"
    print(first_three(s1))
    print(first_three(s2))