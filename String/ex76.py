from ex2 import num_char
#  Write a Python program to count the number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters.

def count_substr_lower(s, n):
    a = num_char(s)
    one = ""
    l = []
    con = []
    for j,i in a.items():
        if i == 1 and j.islower():
            one = one + j
    for i in one:
        l.append(s.find(i))

  
    for i,j in zip(l,l[1:]):
        if i + 1 == j:
            con.append((i,j))
    for i in con:
        if len(i) == n:
            return len(con)
        

        
if __name__ == "__main__":
    s = "abCdefGahidjk"
    n = 2
    print(count_substr_lower(s, n))
    