import string
# Write a Python program to remove punctuation from a given string.
# Sample Output:
# Original text:
# String! With. Punctuation?
# After removing Punctuations from the said string:
# String With Punctuation
def remove_punctuation(s):
    for i in string.punctuation:
        s = s.replace(i, "")
    return s

if __name__ == "__main__":
    s = "String! With. Punctuation?"
    print(remove_punctuation(s))