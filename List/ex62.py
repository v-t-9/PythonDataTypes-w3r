# Write a Python program to print a list of space-separated elements.

if __name__ == "__main__":
    l = [1,2,3,4,5,6]
    for i in l:
        print(i, end= " ")
    # other option
    # print(*l)