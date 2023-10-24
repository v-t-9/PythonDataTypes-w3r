# Write a Python program to determine the index of a given string at which a certain substring starts. If the substring is not found in the given string return 'Not found'.

def index_start_substring(s, su):
    if su in s:
        return s.index(su)
    else: 
        return "Not found"

if __name__ == "__main__":
    s = "Python Exercises"
    su1 = "Ex"
    su2 = "ab"
    print(index_start_substring(s, su1))
    print(index_start_substring(s, su2))