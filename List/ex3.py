# Write a Python program to get the largest number from a list.
def largest_num(l):
    res = 0
    for i in l:
        if i >= res:
            res = i
    return res

if __name__ == "__main__":
    l = [10, 22, 45, 120, 60, 400] 
    print(largest_num(l))