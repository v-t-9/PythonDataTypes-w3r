from ex96 import eliminate_special_chars, separate_words_upper, unite_single_str
# Write a Python program to convert a given string to Snake case.


def str_to_snake_case(s):
    l = unite_single_str(separate_words_upper(eliminate_special_chars(s)).lower().split()).split()
    
    res = l[0]
    for i in range(1, len(l)):
        res = res + "_" + l[i] 
     
    return res
    

if __name__ == "__main__":
    s1 = "JavaScript"
    s2 = "Foo-Bar"
    s3 = "foo_bar"
    s4 = "--foo.bar"
    s5 = "fooBAR"
    s6 = "foo bar"
    print(str_to_snake_case(s1))
    print(str_to_snake_case(s2))
    print(str_to_snake_case(s3))
    print(str_to_snake_case(s4))
    print(str_to_snake_case(s5))
    print(str_to_snake_case(s6))