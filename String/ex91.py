# Write a Python program to convert a given heterogeneous list of scalars into a string.
# Sample Output:
# Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False

def list_to_str(l):
    r = " "
    for i in range(len(l)-1):
        r = r + str(l[i]) + ", "
    r = r + str(l[-1])
    return r

if __name__ == "__main__":
    l = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
    print(list_to_str(l))