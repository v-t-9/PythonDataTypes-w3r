# Write a Python program to get the frequency of elements in a list.
def frecuency_elements(l):
    res = dict()
    for i in l:
        res[i] = l.count(i)
    return res
if __name__ == "__main__":
    l = [1, 1, 1, 2, 3, 3, "a", "b", "b", "b", "a"]
    print(frecuency_elements(l))