# Write a Python program to find the index of an item in a specified list.

def find_index(l, item):
    for i in range(len(l)):
        if item == l[i]:
            return i
if __name__ == "__main__":
    l = ["p", "y", "t", "h", "o", "n"]
    item = "o"
    print(find_index(l, item))