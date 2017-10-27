def main():
    start_monthStr = input("In what month did you start school?  ")
    lengthStr = input("How many months will you spend in college?  ")
    start_month = int(start_monthStr)
    length = int(lengthStr)
    final_month = (length + start_month) % 12
    print("You'll graduate in month number %d" % final_month)

main()
