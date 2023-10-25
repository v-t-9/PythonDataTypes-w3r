# Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
# Sample Output: 
# (255, 165, 1)
# (255, 255, 255)
# (0, 0, 0)
# (255, 0, 0)
# (0, 0, 128)
# (192, 192, 192)

def hex_rgb(s):
    st = ""
    for i in range(len(s)):
        if i%2 ==0:
            st = st + "," + s[i] 
        else:
            st = st + s[i]
    l = st.lstrip(",").split(",")
    res = [int(i,16) for i in l]
    return tuple(res)


if __name__ == "__main__":
    s1 = "FFA501"
    s2 = "FFFFFF"
    s3 = "000000"
    s4 = "000080"
    s5 = "C0C0C0"

    print(hex_rgb(s1))
    print(hex_rgb(s2))
    print(hex_rgb(s3))
    print(hex_rgb(s4))
    print(hex_rgb(s5))
