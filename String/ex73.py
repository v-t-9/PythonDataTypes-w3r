# Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.

def count_char_upper(s):
    c = 0
    for  i in s:
        if i.isalpha():
            if i.isupper():
                c = c + 1
    return c

def count_char_lower(s):
    c = 0
    for  i in s:
        if i.isalpha():
            if i.islower():
                c = c + 1
    return c

def count_char_num(s):
    c = 0
    for  i in s:
        if i.isnumeric():
            c = c +1
    return c

def count_char_special(s):
    return  len(s)  - count_char_num(s) - count_char_lower(s) - count_char_upper(s)
    

if __name__ == "__main__":
    s = "ab5c/DE#f3gHI!!!12"
    print("Nuumber of uppercase characters {}\nNumber of lowercase characters {}\nNumber of numeric characters {}\nNumber of special characters: {}".format(count_char_upper(s), count_char_lower(s), count_char_num(s), count_char_special(s)))