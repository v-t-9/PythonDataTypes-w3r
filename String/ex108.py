# Write a Python program that takes a string and returns - on both sides of each element, which are not vowels.
# Sample Data:
# ("Green") -> "-G--r-ee-n-"
# ("White") -> "-W--h-i-t-e"
# ("aeiou") -> "aeiou"

def add_symbol_if_not_vowel(s):
    res = ""
    for i in s:
        if i in "aeiou" or i in "AEIOU":
            res = res + i
        else:
            res = res + "-" + i + "-"
    return res

if __name__ == "__main__":
    s1 = "Green"
    s2 = "White"
    s3 = "aeiou"
    print(add_symbol_if_not_vowel(s1))
    print(add_symbol_if_not_vowel(s2))
    print(add_symbol_if_not_vowel(s3))