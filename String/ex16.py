#  Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

insert_string_middle = lambda s,w: s[:2] + w + s[len(s)-2:]

if __name__ == "__main__":
    w1 = "Python"
    s1 = "[[]]"
    w2 = "PHP"
    s2 = "{{}}"
    print(insert_string_middle(s1,w1))
    print(insert_string_middle(s2,w2))