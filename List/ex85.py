# Write a Python program to create a multidimensional list (lists of lists) with zeros.
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

if __name__ == "__main__":
    l =  []
    for i in range(3):
        l.append([])
        for j in range(2):
            l[i].append(0)
    print(l)