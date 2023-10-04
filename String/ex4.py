# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
def change_occurrences_first_char(s):
    pos = []
    res = " "
    for i in range(1,len(s)):
        if s[0] == s[i]:
            pos.append(i)
    for i in range(len(s)):
        if i in pos:
            res = res + "$"
        else:
            res = res + s[i]
    return res

if __name__ == "__main__":
    s = "restart"
    print(change_occurrences_first_char(s))