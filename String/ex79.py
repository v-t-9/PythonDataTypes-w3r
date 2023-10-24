# Write a Python program to find the smallest and largest words in a given string.

def smallest_largest_word(s):
    l = s.split()
    le = [len(i) for i in l ]
    ma = max(le)
    mi = min(le)
    return l[le.index(mi)] , l[le.index(ma)]

if __name__ == "__main__":
    s = "red blue orange green"
    print(smallest_largest_word(s))