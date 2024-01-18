# Write a Python program to remove specific words from a given list.
# Original list:
# ['red', 'green', 'blue', 'white', 'black', 'orange']
# Remove words:
# ['white', 'orange']
# After removing the specified words from the said list:
# ['red', 'green', 'blue', 'black']

def remove_from_list(l, r):
    for i in r:
        l.remove(i)
    return l

if __name__ == "__main__":
    l = ['red', 'green', 'blue', 'white', 'black', 'orange']
    r = ['white', 'orange']
    print(remove_from_list(l,r))