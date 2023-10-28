# Write a Python function that takes two lists and returns True if they have at least one common member.
def list_common_element(l1,l2):
    for i in l1:
        if i in l2:
            return True
    return False

if __name__ == "__main__":
    l1 =["a", "b", 1, 2, 555, 227]
    l2 =["c", "b", 1, 22]
    l3 =["a", "d", 12, 555, 227]
    print(list_common_element(l1,l2))
    print(list_common_element(l3,l2))
