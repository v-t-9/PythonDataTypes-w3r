#  Write a Python program to get the frequency of elements in a given list of lists.
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Frequency of the elements in the said list of lists:
# {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

def frequency_elements(l):
    d = dict()
    li = [j for i in l for j in i]
    for i in range(len(li)):
            d[li[i]] = li.count(li[i])
    return d

if __name__ == "__main__":
    l = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
    print(frequency_elements(l))