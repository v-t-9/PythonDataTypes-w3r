# Write a Python program to check whether all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

def empty_dicts(l):
    r = []
    for i in l:
        if i == {}:
            r.append(True)
        else:
            r.append(False)
    return all(r)

if __name__ == "__main__":
    l1 = [{},{},{}]
    l2 = [{1,2},{},{}]
    print(empty_dicts(l1))
    print(empty_dicts(l2))
