# Write a Python program to find the smallest window that contains all characters in a given string.
def contains_all_char(s):
   le = len(s)
   r = []
   if le <= 1: 
        return s
   for i in set(s):
       if i in s:
           r.append(s.index(i))
   mi = min(r)
   ma = max(r)
   return s[mi:ma+1]


if __name__ == "__main__":
    s = "udwregthyjuwewrdt"
    print(contains_all_char(s))