# Write a Python program to remove key-value pairs from a list of dictionaries.

def remove_pairs(l, r):
    while r in l:
        l.remove(r)
    return l

if __name__ == "__main__":
    l = [{"Black": "#000000"}, {"Red":"#FF0000"}, {"Black": "#000000"}, {"Red":"#FF0000"}]
    remove = {"Black": "#000000"}
    print(remove_pairs(l,remove))

    