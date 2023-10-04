# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def num_char(s):
    r = dict()
    for i in s:
        r[i] = s.count(i)
    return r

if __name__ == "__main__":
    s = "google.com"
    print(num_char(s))