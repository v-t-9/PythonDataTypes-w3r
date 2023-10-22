#  Write a Python program to compute the sum of the digits in a given string.

def sum_digits(s):
    r = 0
    for i in s:
        if i.isdigit():
            r = r + int(i)
    return r

if __name__ == "__main__":
    s = "aas23ddfgdg455"
    print(sum_digits(s))