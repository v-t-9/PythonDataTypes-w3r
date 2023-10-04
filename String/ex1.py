#  Write a Python program to calculate the length of a string.
def len_str(s):
    c = 0
    for i in s:
        c = c + 1
    return c
if __name__ == "__main__":
    s = "Hello"
    print(len_str(s))