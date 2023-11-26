# Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
# Original list:
# [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# Index positions of the maximum value of the said list:
# 7
# Index positions of the minimum value of the said list:
# 3, 11

def index_position_max_min(l):
    mi = min(l)
    ma = max(l)
    mi_ind = []
    ma_ind = []

    for i in range(len(l)):
        if l[i] == mi:
            mi_ind.append(i)
        if l[i] == ma:
            ma_ind.append(i)
    return "Index positions of max value: {}.\nIndex positions of min value {}".format(str(ma_ind), mi_ind)

if __name__ == "__main__":
    l = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
    print(index_position_max_min(l))
