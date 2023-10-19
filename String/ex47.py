# Write a Python program to lowercase the first n characters in a string.

n_char_lowercase = lambda s, n: s[:n].lower() + s[n:]


if __name__ == "__main__":
    n = int(input("Number of characters to lowercase: "))
    s = input("Enter the text: ")
    print(n_char_lowercase(s,n))
