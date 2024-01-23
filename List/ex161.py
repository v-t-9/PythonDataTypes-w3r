# Write a Python program to check if a given list increases strictly. Moreover, if removing only one element from the list results in a strictly increasing list, 
# we still consider the list true.

def increases_strictly(l):
    res = []
    for i , j in list(zip(l,l[1:])):
        if j >i:
            res.append(True)
        else:
            res.append(False)

    return all(res)


if __name__ == "__main__":
    l1 = [1, 2, 3, 4]
    l2 = [1,2,0,4,3,2]
    print(increases_strictly(l1))
    print(increases_strictly(l2))