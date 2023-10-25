#  Write a Python program to remove duplicate words from a given string.
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution 
def duplicates_words(s):
    x = set()
    l = s.split()
    st = ""
    for i in l:
        if i not in x:
            x.add(i)
            st = st  + i + " "
    return st

if __name__ == "__main__":
    s = "Python Exercises Practice Solution Exercises"
    print(duplicates_words(s))
    