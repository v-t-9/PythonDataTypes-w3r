# Write a Python program to print the index of a character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

if __name__ == "__main__":
    s = "Python"
    for i in range(len(s)):
        print("Character: ", s[i], " Position: ", i)
