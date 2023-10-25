# Write a Python program to find the common values that appear in two given strings.
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python
def common_values(s1,s2):
    r = ""
    for i in s1:
        if i in s2:
            r = r + i
    return r


if __name__ == "__main__":
    s1 = "Python3"
    s2 = "Python2.7"
    print(common_values(s1,s2))