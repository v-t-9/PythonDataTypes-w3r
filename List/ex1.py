# Write a Python program to sum all the items in a list.
def sum_num(l):
    res = 0
    for i in l:
        res = res + i
    return res
if __name__ == "__main__":
    l = [10, 22, 45, 120] 
    print(sum_num(l))