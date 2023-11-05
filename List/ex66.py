# Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
def highest_sum(l):
    su = [sum(i) for i in l]
    for i in l:
        if max(su) == sum(i):
            return i
    
if __name__ == "__main__":
    l = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    print(highest_sum(l))