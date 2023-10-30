# Write a Python program to generate all sublists of a list.

def all_sublists(l):
    res = []
    for start in range(len(l)):
        for end in range(start + 1, len(l) + 1):
            res.append(l[start:end])
    return res

if __name__ == "__main__":
    l = ["a", "b", "c"]
    print(all_sublists(l))