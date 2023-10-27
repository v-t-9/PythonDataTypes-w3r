#  Write a Python program that capitalizes the first letter and lowercases the remaining letters in a given string.
# Sample Data:
# ("Red Green WHITE") -> "Red Green White"
# ("w3resource") -> "W3resource"
# ("dow jones industrial average") -> "Dow Jones Industrial Average"
def capitalize_first_letter(s):
    r = ""
    for i in s.split():
        r = r + i.capitalize() + " "

    return r
if __name__ == "__main__":
    s1 = "Red Green WHITE"
    s2 = "w3resource"
    s3 = "dow jones industrial average"
    print(capitalize_first_letter(s1))
    print(capitalize_first_letter(s2))
    print(capitalize_first_letter(s3))