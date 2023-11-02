# Write a Python program to print nested lists (each list on a new line) using the print() function.

if __name__ == "__main__":
    l = [[1,2,3],["a", "b", "c"],[3,4,5],["d", "e", "f"]]
    print("\n".join([str(i) for i in l]))
    