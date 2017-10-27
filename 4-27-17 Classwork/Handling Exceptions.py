import  math
num = ''
while not isdigit(num):
    num = input('Please Enter a number that isn\'t zero:  ')
num = int(num)
if num != 0:
    better_num = 5/num * -1
    if better_num >= 0:
        even_better_num = math.sqrt(better_num)

def noError(param):
    i = 0
    try:
        size = len(param)
        while i < size:
            print(param[i])
            i += 1
    except:
        print('The wrong kind of parameter was given')
