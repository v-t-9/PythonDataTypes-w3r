#  Write a Python program to convert a list of characters into a string.

def convert_to_string(l):
    res = ""
    for i in l:
        res = res + i
    return res
if __name__ == "__main__":
    l = ["p", "y", "t", "h", "o", "n"]
    print(convert_to_string(l))