from ex2 import num_char
# Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.

def strings_occurrence_char(s):
    a = num_char(s)
    mul = ""
    one = ""
    for j,i in a.items():
        if i > 1:
             mul = mul + j
        if i == 1:
            one = one + j
    
    return "String with characters that occur only once: {} \nString with characters that occur multiple times: {}".format(one, mul)
if __name__ == "__main__":
    s = "abbbccccdeff"
    print(strings_occurrence_char(s))