# Write a Python program to access the index of a list.
def access_index_list(l):
    ind = []
    for i in range(len(l)):
        ind.append(i)
    res = list(zip(ind,l))
    return res
if __name__ == "__main__":
    l = [32,45,67,98,102,2045]
    print(access_index_list(l))