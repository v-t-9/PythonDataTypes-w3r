# Write a Python program to split a multi-line string into a list of lines.
# Sample Output:
# Original string: This
# is a
# multiline
# string.
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']


if __name__ == "__main__":
    s = """This
            is a
            multiline
            string."""
    
    print(s.split())