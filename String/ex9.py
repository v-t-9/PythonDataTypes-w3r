# Write a Python program to remove the nth index character from a nonempty string.

def remove_nth_index_char(s,n):
    if len(s)>=n:
        return s[:n] + s[n+1:]
    else:
        return f"n is bigger than the length of the string"


if __name__ == "__main__":
    s = "Python"
    n = 2
    print(remove_nth_index_char(s,n))
