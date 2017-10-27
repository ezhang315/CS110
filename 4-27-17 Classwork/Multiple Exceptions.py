import math
try:
    num = int(input('Please enter a number: '))
    better_num = 5 / num
    even_better_num = math.sqrt(-1)

except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
