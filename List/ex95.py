# Write a Python program to sort each sublist of strings in a given list of lists.

def sort_each_sublist(l):
    r = list(map(sorted,l))
    return r
if __name__ == "__main__":
    l =  [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
    print(sort_each_sublist(l))