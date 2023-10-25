# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
# Sample Output:
# Input the string: W3resource
# ['Valid string.']
def check_upper_lower_num(s):
    r = []
    if any(i.isnumeric() for i in s):
        r.append(True)
    else:
        r.append(False)

    if any(i.isupper() for i in s):
        r.append(True)
    else:
        r.append(False)

    if any(i.islower() for i in s):
        r.append(True)
    else:
        r.append(False)
             
    if all(r):
        return f"Valid string"
    else:
       return f"The string isn't valid"
    
    

if __name__ == "__main__":
    s = "W3resource"
    s1 = "Python"
    print(check_upper_lower_num(s))
    print(check_upper_lower_num(s1))