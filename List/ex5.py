# Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def str_len_first_last(l):
    c  = 0 
    for i in l:
        if len(i) >=2 and i[0] == i[-1]:
            c = c + 1
    return c
if __name__ == "__main__":
    l = ['abc', 'xyz', 'aba', '1221']
    print(str_len_first_last(l))