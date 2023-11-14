# Write a Python program to decode a run-length message.
# Original encoded list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Decode a run-length encoded said list:
# [1, 1, 2, 3, 4, 4, 5, 1]

def decode_list(l):
    res = []
    for i in l:
        if type(i) is list:
            for j in range(i[0]):
                res.append(i[1])
        else:
            res.append(i)
    return res

if __name__ == "__main__":
    l = [[2, 1], 2, 3, [2, 4], 5, 1]
    print(decode_list(l))