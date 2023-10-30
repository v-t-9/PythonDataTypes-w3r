# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

concatenate_list_range = lambda n, l:  ["{}{}".format(j,i) for i in range(1,n+1) for j in l]
 


if __name__ == "__main__":
    n = 5 
    l = ['p', 'q']
    print(concatenate_list_range(n,l))