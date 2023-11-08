# Write a Python program to find items starting with a specific character from a list.
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
# []
def find_item_starts_with_char(l, ch):
    res = []
    for i in l:
        if i.startswith(ch):
            res.append(i)
    return res

if __name__ == "__main__":
    l = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
    char1 = "a"
    char2 = "d"
    char3 = "w"
    print(find_item_starts_with_char(l,char1))
    print(find_item_starts_with_char(l,char2))
    print(find_item_starts_with_char(l,char3))