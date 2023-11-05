#  Write a Python program to iterate over two lists simultaneously.

if __name__ == "__main__":
    letters = ["a", "b", "c", "d"]
    numbers = [1,2,3,4]

    for i, j in zip(letters, numbers):
        print(i,j)
