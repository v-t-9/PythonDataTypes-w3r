#  Write a Python program to check if all items in a given list of strings are equal to a given string.

def items_equal_string(s,l):
    if s in l:
        if len(set(l)) == 1:
            return True
        else:
            return False
    else:
        return "The string isn't in the list"

if __name__ == "__main__":
    s = "a"
    l1 = ["a", "b", "c", "d"]
    l2 = ["a", "a", "a", "a"]
    print(items_equal_string(s,l1))
    print(items_equal_string(s,l2))
