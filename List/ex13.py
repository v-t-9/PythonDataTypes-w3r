# Write a Python program to generate a 3*4*6 3D array whose each element is *.
def array_3d():
    return [[ ['*' for i in range(6)] for j in range(4)] for k in range(3)]

if __name__ == "__main__":
    print(array_3d())