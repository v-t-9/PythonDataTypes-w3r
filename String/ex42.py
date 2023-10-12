from ex2 import num_char
# Write a Python program to count repeated characters in a string.

def repeated_char(s):
    ch = num_char(s)
    d = dict()
    for i,j in ch.items():
        if j >1:
            d[i] = j
    return d
if __name__ == "__main__":
    s = "thequickbrownfoxjumpsoverthelazydog"
    print(repeated_char(s))