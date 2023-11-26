# Write a Python program to check if two lists have the same elements in them in same order or not.
# Original lists:
# ['red', 'green', 'black', 'orange']
# ['red', 'pink', 'green', 'white', 'black']
# ['white', 'orange', 'pink', 'black']
# Test common elements between color1 and color2 are in same order?
# True
# Test common elements between color1 and color3 are in same order?
# False
# Test common elements between color2 and color3 are in same order?
# False

def order_common_elements(l1,l2):
    li = []
    for i in l1:
        if i in l2:
            li.append(i)
    for i in l2:
        if i in l1:
            li.append(i)

    r1 = [ i for i in l1 if i in list(set(li))]
    r2 = [ i for i in l2 if i in list(set(li))]
    if r1 == r2:
        return True
    else:
        return False
    
   
    

if __name__ == "__main__":
    l1 = ['red', 'green', 'black', 'orange']
    l2 = ['red', 'pink', 'green', 'white', 'black']
    l3 = ['white', 'orange', 'pink', 'black']
    print(order_common_elements(l1,l2))
    print(order_common_elements(l1,l3))
    print(order_common_elements(l2,l3))
