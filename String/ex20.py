# Write a Python function to reverse a string if its length is a multiple of 4.
def reverse_multiple_four(s):
    if len(s) % 4 == 0:
        return s[::-1]
    return s


if __name__ == "__main__":
    s1 = "abcd"
    s3= "abcde"
    print(reverse_multiple_four(s1))
    print(reverse_multiple_four(s3))