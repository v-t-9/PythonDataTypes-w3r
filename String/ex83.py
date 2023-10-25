# Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001

if __name__ == "__main__":
    s = 25
    print("{0:d}\t{0:o}\t{0:x}\t{0:b}".format(s))