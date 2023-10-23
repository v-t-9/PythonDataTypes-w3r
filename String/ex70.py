# Write a Python program that concatenates uncommon characters from two strings
def uncommon_characters(s1,s2):
    res = ""
    m = max([len(s1), len(s2)])

    for i in s1:
        if i not in s2:
            res = res + i
    for i in s2:
        if i not in s1:
            res = res + i
    return res


if __name__ == "__main__":
    s1 = "abcdsiofmh"
    s2 = "mhzabcdnpxbd"
    print(uncommon_characters(s1,s2))