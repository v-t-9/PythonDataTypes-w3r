# Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

def mul_int_to_single_int(l):
    res = ""
    for i in l:
        res = res + str(i)
    return int(res)
if __name__ == "__main__":
    l = [11, 33, 50]
    print(mul_int_to_single_int(l))