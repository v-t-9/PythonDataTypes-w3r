# Write a Python program to find a tuple, the smallest second index value from a list of tuples.

def smallest_second_index_value(l):
    min_second_value = min([i[1] for i in l for j in i])
    for i in l:
        if min_second_value == i[1]:
            return i

if __name__ == "__main__":
    l = [(5,2), (1,5), (8,1), (2,8)]
    print(smallest_second_index_value(l))