# Write a Python program to check whether the n-th element exists in a given list.
def element_exists(l,p):
    if len(l)-1 < abs(p):
        return "There isn't an element in the {} position".format(p)
    else:
        return "The element in the {} position is {}".format(p, l[p])
if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10]
    p = -3
    print(element_exists(l,p))