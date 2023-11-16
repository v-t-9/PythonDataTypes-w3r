# Write a Python program to extract specified size of strings from a give list of string values.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

def extract_size_strings(l, size):
    res = [i for i in l if len(i)==size]
    return res
if __name__ == "__main__":
    l = ['Python', 'list', 'exercises', 'practice', 'solution']
    length = 8
    print(extract_size_strings(l,length))