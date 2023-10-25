# Write a Python program to swap cases in a given string.
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY

swap_cases = lambda s: s.swapcase()

if __name__ == "__main__":
    s1 = "Python Exercises"
    s2 = "Java"
    s3 = "NumPy"
    print(swap_cases(s1))
    print(swap_cases(s2))
    print(swap_cases(s3))