# Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
# Original list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Dfference between elements (n+1th - nth) of the said list :
# [1, 1, 1, 1, 1, 1, 1, 1, 1]
# Original list:
# [2, 4, 6, 8]
# Dfference between elements (n+1th - nth) of the said list :
# [2, 2, 2]
def difference_between_consecutive_elements(l):
    res = []
    for i,j in zip(l,l[1:]):
        diff = abs(i-j)
        res.append(diff)
    return res
if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [2, 4, 6, 8]
    print(difference_between_consecutive_elements(l1))
    print(difference_between_consecutive_elements(l2))