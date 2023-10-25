# Write a Python program to remove unwanted characters from a given string.
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises
# Original String : A%^!B#*CD
# After removing unwanted characters:
# ABCD
def remove_unwanted_chars(s):
    r = ""
    for i in s:
        if i.isalpha() or i == " ":
            r = r + i
    return r
if __name__ == "__main__":
    s1 = "Pyth*^on Exercis^es"
    s2 = "A%^!B#*CD"
    print(remove_unwanted_chars(s1))
    print(remove_unwanted_chars(s2))