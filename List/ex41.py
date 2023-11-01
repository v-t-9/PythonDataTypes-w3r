# Write a Python program to create multiple lists.

def multiple_lists():
    lists = dict()
    for i in range(1,11):
        lists[i] = []
    return lists

if __name__ == "__main__":
    print(multiple_lists())