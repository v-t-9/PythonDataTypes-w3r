# Write a Python program to replace each character of a word of length five and more with a hash character (#).
# Sample Output:
# Original string: Count the lowercase letters in the said list of words:
# Replace words (length five or more) with hash characters in the said string:
# ##### the ######### ####### in the said list of ######
# Original string: Python - Remove punctuations from a string:
# Replace words (length five or more) with hash characters in the said string:
# ###### - ###### ############ from a #######


def replace_len_5(s):
    l = s.split()
    r = " "
    for i in l:
        if len(i) >= 5:
            t = "#"*len(i)
            r = r + t + " "
        else:
            r = r + i + " "
                
    return r
if __name__ == "__main__":
    s1 = "Count the lowercase letters in the said list of words"
    s2 = "Python - Remove punctuations from a string"
    print(replace_len_5(s1))
    print(replace_len_5(s2))