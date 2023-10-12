# Write a Python program to count occurrences of a substring in a string.

occurrences_string = lambda s,su: s.count(su)

if __name__ == "__main__":
    s = "abcdefabcdefabcdefab"
    substr = "ab"
    print(occurrences_string(s, substr))
    


