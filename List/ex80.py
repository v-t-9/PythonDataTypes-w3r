# Write a Python program to insert an element at a specified position into a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]

def insert_element_k_position(l,ele,k):
    l.insert(k,ele)
    return l
if __name__ == "__main__":
    l = [1, 1, 2, 3, 4, 4, 5, 1]
    ele = 12
    k = 2
    print(insert_element_k_position(l,ele,k))