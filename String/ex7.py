# Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def find_replace(s):
    
    if ("not" and "poor") in s:
        p = s.find("poor")
        n = s.find("not")
        if (n < p) and n>0 and p >0:
            r = s.replace(s[n:p+4], "good")
            return r
    return s
    
if __name__ == "__main__":
    s1 = "The lyrics is not that poor!"
    s2 = "The lyrics is poor!"
    print(find_replace(s1))
    print(find_replace(s2))
    