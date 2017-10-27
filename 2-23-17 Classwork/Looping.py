# Part 1
def loop1():
    i = 0
    while i < 1000000:
        if vault.tryCode(i):
            return i
        i += 1
        return -1

def loop2():
    count = 0
    i = 0
    j = 0
    while (i < 100):
        j = i
        count = i + 10
        i = count + 1
        i = j
    return -1

 # Part 2
def indefiniteFor():
    for i in range(1):
        x = 0
        while x > 10:
            print('Gotcha!')

def definiteWhile():
    num = 0
    while num <= 30:
        num += 1

# Part 3
def threenplus1(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        print(n)

def main():
    threenplus1(865)
main()
