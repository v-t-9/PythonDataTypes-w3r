#  Write a Python program to generate combinations of n distinct objects taken from the elements of a given list.
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]

def combinations(l):
    res = []
    for i in l:
        for j in l[i:]:
            res.append([i,j])
    
    return res

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(combinations(l))
    print(len(combinations(l)))
