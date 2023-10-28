# Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
# Sample Data:
# ("1981-1991") -> 2
# ("2000-2020") -> 6
def count_leap_years(y1,y2):
    res = 0
    for i in range(int(y1),int(y2)+1,1):
        if i % 4 == 0 and (i % 400 == 0 or i % 100 !=0):
            res = res + 1
    return res


if __name__ == "__main__":
    y1 = "1981"
    y2 = "1991"
    y3 = "2000"
    y4 = "2020"
    print(count_leap_years(y1,y2))
    print(count_leap_years(y3,y4))