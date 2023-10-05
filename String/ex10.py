# Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.


change_first_last_char = lambda s: s[-1] + s[1:-1] + s[0]
if __name__ == "__main__":
    s = "python"
    print(change_first_last_char(s))