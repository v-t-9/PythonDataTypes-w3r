#  Write a Python program to calculate the product of the unique numbers in a given list.
# Original List : [10, 20, 30, 40, 20, 50, 60, 40]
# Product of the unique numbers of the said list: 720000000
def product_unique_num(l):
    li = list(set(l))
    res = 1
    for i in li:
        res = res * i
    return res

if __name__ == "__main__":
    l = [10, 20, 30, 40, 20, 50, 60, 40]
    print(product_unique_num(l))