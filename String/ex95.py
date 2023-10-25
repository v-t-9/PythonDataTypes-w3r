# Write a Python program to convert the values of RGB components to a hexadecimal color code.
# Sample Output:
# FFA501
# FFFFFF
# 000000
# 000080
# C0C0C0

def rgb_hex(t):
    res = "#"
    for i in t:
        res = res + "{:02x}".format(i)
    return res.upper()

if __name__ == "__main__":
    t1 = (255, 165, 1)
    t2 = (255, 255, 255)
    t3 = (0, 0, 0)
    t4 = (255, 0, 0)
    t5 = (0, 0, 128)
    t6 = (192, 192, 192)
    print(rgb_hex(t1))
    print(rgb_hex(t2))
    print(rgb_hex(t3))
    print(rgb_hex(t4))
    print(rgb_hex(t5))
    print(rgb_hex(t6))