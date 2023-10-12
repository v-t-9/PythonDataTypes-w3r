#  Write a Python program to display a number in left, right, and center aligned with a width of 10

if __name__ == "__main__":
    n = 50
    print(f"Left: {n:<10d}")
    print(f"Right: {n:^10d}")
    print(f"Center: {n:>10d}")