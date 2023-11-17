#  Write a Python program to remove duplicate dictionary entries from a given list.
# Original list with duplicate dictionary:
# [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# After removing duplicate dictionary of the said list:
# [{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

def remove_duplicates(l):
    keys = []
    values = []
    res = []
    for i in l:
        for j,k in i.items():
            if j not in keys:
                keys.append(j)
                values.append(k)
    res = [{k:v} for k,v in zip(keys,values)]
    return res
      
    
if __name__ == "__main__":
    l = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
    print(remove_duplicates(l))