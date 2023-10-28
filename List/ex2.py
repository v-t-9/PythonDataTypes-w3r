#  Write a Python program to multiply all the items in a list.

def multiply_num(l):
    res = 1
    for i in l:
        res = res * i
    return res
if __name__ == "__main__":
    l = [10, 22, 45, 120] 
    print(multiply_num(l))