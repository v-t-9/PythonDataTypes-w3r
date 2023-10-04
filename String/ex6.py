# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def add_ending_str(s):
    if len(s)<3:
        return s
    elif s[3:] == "ing":
        return s + "ly"
    else:
        return s + "ing"

if __name__ == "__main__":
    s1 = "abc"
    s2 = "string"
    s3 = "yz"

    print(add_ending_str(s1))
    print(add_ending_str(s2))
    print(add_ending_str(s3))