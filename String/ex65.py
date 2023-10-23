# Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".

def common_char(s1,s2):
    l = []
    for i in s1.lower():
        if i in s2.lower():
            l.append(i)
    if l == []:
        return "No common characters"
    return sorted(l)
    


if __name__ == "__main__":
    s1 = "zAbc"
    s2 = "aBdz"
    s3 = "efG"
    print(common_char(s1,s2))
    print(common_char(s1,s3))