# Write a Python program to flatten a shallow list.
flatten_shallow_list = lambda l: [j for i in l for j in i]


if __name__ == "__main__":
    l =  [[2,4,3],[1,5,6], [9], [7,9,0]]
    print(flatten_shallow_list(l))