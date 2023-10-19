# Write a Python program to split a string on the last occurrence of the delimiter.


if __name__ == "__main__":
    s = "a.b.c.d.e.f.g"
    print(s.rsplit(".")[-1])
    print(s[:len(s)-1].rstrip("."))
