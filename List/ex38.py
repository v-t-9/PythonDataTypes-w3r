# Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def change_position(l):
    r = [(l[i], l[i]+1) for i in range(len(l)) if i % 2 ==0 ]
    r1 = [i[::-1] for i in r]
    res = [j for i in r1 for j in i]
    return res

if __name__ == "__main__":
    l = [0,1,2,3,4,5]
    print(change_position(l))