# Write a Python program to check if a list is empty or not.
def check_list_empty(l):
    if not l:
        return True
    return False
if __name__ == "__main__":
    l1 = []
    l2 =["a", "b", 1, 2]
    print(check_list_empty(l1))
    print(check_list_empty(l2))