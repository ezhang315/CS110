def easterDate(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = (((19 * a) + b) - (b // 4) - ((b - ((b + 8) // 25) + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    if 1900 <= year < 2100:
        return "The date of Easter in %d is %d/%d" % (year, month, day)
    else:
        print("The year you entered was out of range")
        return easterDate(int(input("Try again, between 1900 and 2100 this time please:   ")))
        
def main():
    year = int(input("In what year (between 1900 and 2100) do you want to know the date of Easter?  "))
    print(easterDate(year))

main()
