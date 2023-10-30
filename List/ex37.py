# Write a Python program to find common items in two lists

def common_items(l1,l2):
    se1 = list(set(l1))
    se2 = list(set(l2))
    res = [i for i in se1 if i in se2]
    return res
if __name__ == "__main__":
    l1 = [4,5,3,1,2,6,7,7,2,6]
    l2 = [8,6,7,5,9,10,8,10,11,12]
    print(common_items(l1,l2))