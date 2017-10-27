def multiply(num1, num2):
    accum = 0
    for i in range(num2):
            accum = accum + num1
    return accum

def power(num1, power):
    accum = 1
    for i in range(power):
        accum = accum * num1
    return accum

def square(num):
    return multiply(num, num)

def main():
    print(multiply(12, 11))
    print(power(2, 5))
    print(square(20))

main()
    
    
