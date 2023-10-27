# Write a Python program to remove duplicate characters from a given string.

def duplicates_chars(s):
    x = set()
    st = ""
    for i in s:
        if i not in x:
            x.add(i)
            st = st  + i
        
    return st

if __name__ == "__main__":
    s = "aabbcc"
    print(duplicates_chars(s))