from ex61 import duplicates_chars
# Write a Python program to check whether any word in a given string contains duplicate characters or not. Return True or False.
# Sample Output:
# Original text:
# Filter out the factorials of the said list.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# Python Exercise.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# The wait is over.
# Check whether any word in the said sting contains duplicate characrters or not!
# True

def check_words_contain_duplicate_chars(s):
    l = s.split()
    res = ""
    for i in l:
        res = res + " " + duplicates_chars(i)
    
    if res.strip() == s:
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = "Filter out the factorials of the said list."
    s2 = "Python Exercise."
    s3 = "The wait is over."
    print(check_words_contain_duplicate_chars(s1))
    print(check_words_contain_duplicate_chars(s2))
    print(check_words_contain_duplicate_chars(s3))