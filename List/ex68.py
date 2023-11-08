#  Write a Python program to extend a list without appending.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

if __name__ == "__main__":
    l1 = [10, 20, 30]
    l2 = [40, 50, 60]
    res = l1 + l2
    print(res)