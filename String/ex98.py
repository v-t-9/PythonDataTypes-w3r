# Write a Python program to decapitalize the first letter of a given string.
# Sample Output:
# java Script
# python

decapitalize_1st_letter = lambda s: s[0].lower() + s[1:]

if __name__ == "__main__":
    s1 = "Java Script"
    s2 = "Python"
    print(decapitalize_1st_letter(s1))
    print(decapitalize_1st_letter(s2))
