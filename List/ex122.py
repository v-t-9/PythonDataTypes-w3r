# Write a Python program to find common elements in a nested list.
# Original lists:
# [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
# Common element(s) in nested lists:
# [18, 12]

def common_elements(l):
     res = []
     for i in l[0]:
        if all(i in subl for subl in l[1:]):
            res.append(i)
     return res
if __name__ == "__main__":
     l =  [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
     print(common_elements(l))