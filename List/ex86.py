# Write a Python program to create a 3X3 grid with numbers.
# 3X3 grid with numbers:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

if __name__ == "__main__":
    l =  []
    for i in range(3):
        l.append([])
        for j in range(1,4):
            l[i].append(j)
    print(l)