# Write a Python program to find the last occurrence of a specified item in a given list.
# Original list:
# ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
# Last occurrence of c in the said list:
# 15
# Last occurrence of k in the said list:
# 14
# Last occurrence of w in the said list:
# 12

def last_occurrence(l, ch):
    s = ""
    for i in l:
          s = s + i
    
    return s.rindex(ch)


if __name__ == "__main__":
     l = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
     ch1 = "f"
     ch2 = "c"
     ch3 = "k"
     ch4 = "w"
     print(last_occurrence(l, ch1))
     print(last_occurrence(l, ch2))
     print(last_occurrence(l, ch3))
     print(last_occurrence(l, ch4))
     
     