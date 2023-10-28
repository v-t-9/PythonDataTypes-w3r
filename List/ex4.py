# Write a Python program to get the smallest number from a list.

def smallest_num(l):
    res = max(l)
    for i in l:
        if i <= res:
            res = i
    return res

if __name__ == "__main__":
    l = [10, 22, 45, 120, 60, 400] 
    print(smallest_num(l))