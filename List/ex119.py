# Write a Python program to check if a substring appears in a given list of string values.
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Check if a substring presents in the said list of string values:
# True
# Substring to search:
# abc
# Check if a substring presents in the said list of string values:
# False

def substring_list_strings(l,s):
    for i in l:
        if s in i:
            return True
    return False
         

if __name__ == "__main__":
    l = ['red', 'black', 'white', 'green', 'orange']
    s1 = "ack"
    s2 = "abc"
    print(substring_list_strings(l,s1))
    print(substring_list_strings(l,s2))