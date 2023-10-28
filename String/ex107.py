# Write a Python program that takes two strings. Count the number of times each string contains the same three letters at the same index.
# Sample Data:
# ("Red RedGreen") -> 1
# ("Red White Red White) -> 7
# ("Red White White Red") -> 0


def divide_str_3_chars(s):
    r = []
    for i in range(0,len(s.strip()),3):
        r.append(s.strip()[i:i+3])
    return r

def same_letters_same_index(s1,s2):
    res = 0
 
    l1 = divide_str_3_chars(s1)
    l2 = divide_str_3_chars(s2)
    for i,j in zip(l1,l2):
        if i == j:
            res = res + 1
    return res

if __name__ == "__main__":
    s1 = "Red"
    s2 = "RedGreen"
    s3 = "Red White"
    s4 = "Red White"
    s5 = "White Red"
    print(same_letters_same_index(s1,s2))
    print(same_letters_same_index(s3,s4))
    print(same_letters_same_index(s4,s5))
   