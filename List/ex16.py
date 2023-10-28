# Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

def first_five_square(n1, n2):
    sq = []
    for i in range(n1,n2+1):
        sq.append(i**2)
    return sq[10:15]


if __name__ == "__main__":
    n1 = 1
    n2 = 30
    print(first_five_square(n1,n2))