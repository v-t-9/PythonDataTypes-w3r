# Write a Python program to strip a set of characters from a string.
def delete_char_string(s,d):
    res = ""
    for i in s:
        if i != d:
            res = res + i
    return res

if __name__ == "__main__":
    s = "abcdefabcdefabcdefabcdefabcdef"
    del_ch= "e"
    print(delete_char_string(s, del_ch))