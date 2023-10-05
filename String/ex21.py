# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.


def convert_upper_if_two_upper_char(s):
    c = 0
    for i in s[:4]:
        if i.isupper():
            c = c + 1
    if c >=2:
        return s.upper()
    return s


if __name__ == "__main__":
    s1 = "AbCde"
    s2 = "abcde"
    print(convert_upper_if_two_upper_char(s1))
    print(convert_upper_if_two_upper_char(s2))