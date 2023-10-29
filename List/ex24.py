# Write a Python program to append a list to the second list.
def append_list_to_other(l1,l2):
    l1.extend(l2)
    return l1
if __name__ == "__main__":
    l1 = [1,2,3]
    l2 = ["a", "b", "c"]
    print(append_list_to_other(l1,l2))