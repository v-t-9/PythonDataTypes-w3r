# Write a Python program to insert an element before each element of a list.
def insert_element_before(l):
    res = []
    for i in l:
        res.append("-")
        res.append(i)
    return res
if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10]
    print(insert_element_before(l))
