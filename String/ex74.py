# Write a Python program to find the minimum window in a given string that will contain all the characters of another given string.
# Example 1
# Input : str1 = " PRWSOERIUSFK "
# str2 = " OSU "
# Output: Minimum window is "SOERIU"

def str_with_char_another_str(s1,s2):
   
    ma = max([len(s1), len(s2)])
    l = []
    if ma == len(s1):
        for i in s1:
            if i in s2:
                l.append(s1.index(i))
        p = sorted(list(set(l)))
        pmi = min(p)
        pma = max(p)
        return s1[pmi:pma+1]

    if ma == len(s2):
        for i in s2:
            if i in s1:
                l.append(s2.index(i))
        p = sorted(list(set(l)))
        pmi = min(p)
        pma = max(p)
    return s2[pmi:pma+1]


if __name__ == "__main__":
    s1 = "PRWSOERIUSFK"
    s2 = "OSU"
    print(str_with_char_another_str(s1,s2))