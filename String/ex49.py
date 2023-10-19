from ex2 import num_char
# Write a Python program to count and display vowels in text.

def vowels(s):
    r = ""
    for i in s.lower():
        if i in "aeiou":
            r = i + r
    return r

if __name__ == "__main__":
    s = "google.com"
    print(num_char(vowels(s)))
    print(sum(num_char(vowels(s)).values()))