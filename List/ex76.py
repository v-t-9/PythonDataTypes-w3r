from ex75 import runlen_encoding, str_to_list
# Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]


def modified_encoding(l):
    li = runlen_encoding(l)
    res = []
    for i in li: 
        if type(i) == list:
            if i[0] == 1:
                res.append(i[1])
            else:
                res.append(i)
    return res
if __name__ == "__main__":
    l = [1, 1, 2, 3, 4, 4, 5, 1]
    s = "aabcddddadnss"
    l1 = str_to_list(s)
    print(modified_encoding(l))
    print(modified_encoding(l1))

  

       

