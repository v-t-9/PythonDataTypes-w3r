import textwrap
# Write a Python program to wrap a given string into a paragraph with a given width.
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox

if __name__ == "__main__":
    s = "The quick brown fox"
    w = 10
    print(textwrap.fill(s, width=w))