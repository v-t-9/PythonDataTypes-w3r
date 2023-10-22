# Write a Python program to move spaces to the front of a given string.
def front_spaces(s):
    c = s.count(" ")
    st = s.replace(" ", "")
    return c*" " + st

if __name__ == "__main__":
    s = "a b c d"
    print(front_spaces(s))