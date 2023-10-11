# Write a Python program to print the following integers with '*' to the right of the specified width.
#n1 = 3
#w1 = 2
#n2 = 123
#w2 = 6
if __name__ == "__main__":
    n1 = 3
    w1 = 2
    n2 = 123
    w2 = 6
    print("Number 1: ", str(n1).ljust(w1, "*"))
    print("Number 2: ", str(n2).ljust(w2,"*"))

    