# Write a Python program to check whether two lists are circularly identical.
def circularly_identical_lists(l1, l2):
    l3 = l1 * 2
    for i in range(0,len(l1)):
        a = 0
        for j in range(i, i+len(l1)):
            if l2[a] == l3[j]:
                a = a + 1
        if a == len(l1):
            return True
    return False
   
if __name__ == "__main__":
    list1 = [10, 10, 0, 0, 10]
    list2 = [10, 10, 10, 0, 0]
    list3 = [1, 10, 10, 0, 0]
    print(circularly_identical_lists(list1, list2))
    print(circularly_identical_lists(list1, list3))