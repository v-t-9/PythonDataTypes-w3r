# Write a Python program to find the first repeated word in a given string.

def first_most_repeated(s):
    x =set()
    for i in s.split(" "):
        if i not in x:
            x.add(i)
        else:
            return i

if __name__ == "__main__":
    s = "red blue orange yellow blue red blue blue"
    print(first_most_repeated(s))