# Write a Python program that takes a string and replaces all the characters with their respective numbers.
# Sample Data:
# ("Python") -> "16 25 20 8 15 14"
# ("Java") -> "10 1 22 1"
# ("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"

def repalce_char_num(s):
    res = ""
    for i in s.lower():
        n = ord(i) -96
        res = res + str(n) + " "
    return res
if __name__ == "__main__":
    s1 = "Python"
    s2 = "Java"
    s3 = "Python Tutorial"
    print(repalce_char_num(s1))
    print(repalce_char_num(s2))
    print(repalce_char_num(s3))
    