# Python program to make two given strings (lower case, may or may not be of the same length) anagrams.
def anagrams(s1,s2):
    r = set()
    if len(s1) >= len(s2):
        for i in s1:
            if i in s2 and i not in r:
                r.add(i)
    elif len(s1) < len(s2):
        for i in s2:
            if i in s1 and i not in r:
                r.add(i)
 
    return "".join(r)
                
if __name__ == "__main__":
    s1 = "tac"
    s2 = "acta"
    print(anagrams(s1,s2))