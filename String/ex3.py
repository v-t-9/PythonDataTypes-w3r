# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
def first_and_last_2char(s):
    if len(s) >=2:
        return s[:2] + s[len(s)-2:]
    else:
        return ""
if __name__ == "__main__":
    s1 = "w3resource"
    s2 = "w3"
    s3 = "w"
    print(first_and_last_2char(s1))
    print(first_and_last_2char(s2))
    print(first_and_last_2char(s3))