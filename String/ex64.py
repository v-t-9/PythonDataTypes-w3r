# Write a Python program to find the maximum length of consecutive 0's in a given binary string.

def max_consecutive_zeros(s):
    l = s.split("1")
    return len(max(l))

if __name__ == "__main__":
    s1 = "1001010000111"
    s2 = "10101"
    print(max_consecutive_zeros(s1))
    print(max_consecutive_zeros(s2))