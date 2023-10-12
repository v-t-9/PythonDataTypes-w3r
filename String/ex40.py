# Write a Python program to reverse words in a string.
def reverse_words_str(s):
    l = s.split()
    return l[::-1]
if __name__ == "__main__":
    s = "one two three four five"
    print(reverse_words_str(s))