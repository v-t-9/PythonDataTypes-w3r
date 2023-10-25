# Write a Python program to convert a given string to Camelcase.
def eliminate_special_chars(s):
    res = ""
    for i in s:
        if i.isalnum():
            res = res + i 
        else: 
            res  = res + " "
    
    return res

def separate_words_upper(s):
    res = ""
    for i in s:
        if i.isupper():
            res = res + " " + i
        else:
            res = res + i
    return res

def unite_single_str(l):
    res = ""
    
    for i in l:
        if len(i) == 1:
            res = res + i
        else:
            res = res + i + " "
    return res



def convert_to_camelcase(s):
    l = unite_single_str(separate_words_upper(eliminate_special_chars(s)).lower().split()).split()
    res = l[0]
    for i in range(1,len(l)):
        res = res + l[i].title()
    return res

if __name__ == "__main__":
    s1 = "JavaScript"
    s2 = "Foo-Bar"
    s3 = "foo_bar"
    s4 = "--foo.bar"
    s5 = "fooBAR"
    s6 = "foo bar"
   
    print(convert_to_camelcase(s1))
    print(convert_to_camelcase(s2))
    print(convert_to_camelcase(s3))
    print(convert_to_camelcase(s4))
    print(convert_to_camelcase(s5))
    print(convert_to_camelcase(s6))