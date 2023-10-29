# Write a Python program to find the second smallest number in a list
def second_smallest_number(l):
    l1 = sorted(list(set(l)))
    return l1[1]
if __name__ == "__main__":
    l1 = [2,5,12,1,45,2,6,12]
    l2 = [-2,-5,4,7,-7,8]
    print(second_smallest_number(l1))
    print(second_smallest_number(l2))