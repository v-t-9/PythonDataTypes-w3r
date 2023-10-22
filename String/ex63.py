#  Write a Python program to remove leading zeros from an IP address.

def remove_leading_zeros(s):
    l = s.split(".")
    st = ""
    for i in l:
        if len(i) > 1 and i.startswith("0"):
            st = st + i.replace("0","") + "."
        else:
            st = st + i + "."
    return st[:len(st)-1] + st[-1].replace(".","")


if __name__ == "__main__":
    s = "127.0.0.01"
    s1 = "255.024.01.01"
    print(remove_leading_zeros(s))
    print(remove_leading_zeros(s1))