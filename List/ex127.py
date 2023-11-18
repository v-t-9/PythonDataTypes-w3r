# Write a Python program to remove words from a given list of strings containing a character or string.
# Original list:
# list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
# Character list:
# ['#', 'color', '@']
# New list:
# ['Red', '', 'Green', 'Orange', 'White']

def reomve_words(l,ch):
    r = []
    for i in l:
        for j in i.split():
            if not any(k in j for k in ch) and j not in r:    
                r.append(j)


    return r
if __name__ == "__main__":
    l = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
    ch = ['#', 'color', '@']
    print(reomve_words(l, ch))
