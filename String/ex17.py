# Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
def insert_end(s):
    if len(s)>=2:
        return s[len(s)-2:]*4
    else:
        return f"The string is too short!"
    

if __name__ == "__main__":
    s1 = "Python"
    s2 = "Exercises"
    print(insert_end(s1))
    print(insert_end(s2))
   