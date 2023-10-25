#  Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]

extract_num = lambda s: [int(i) for i in s.split() if i.isnumeric()]
if __name__ == "__main__":
    s = "red 12 black 45 green"
    print(extract_num(s))