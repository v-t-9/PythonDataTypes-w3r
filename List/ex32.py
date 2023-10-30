#  Write a Python program to check whether a list contains a sublist.
def is_sublist(l1, l2):
    if "".join(l2) in "".join(l1):
        return True
    else:
        return False
if __name__ == "__main__":
    l1 = ["1", "a", "2", "b", "3", "c", "4"]
    l2 = ["4", "d"]
    l3 = ["2", "b"]
    print(is_sublist(l1,l2))
    print(is_sublist(l1,l3))