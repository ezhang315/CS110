import random

def printZero():
    num = int(input("Please enter a number:  "))
    if num < 0:
        num = num + abs(num)
    else:
        num = num + (num * -1)
    print(num)

def guessNumber():
    num = random.randrange(1,11)
    print(num)
    for i in range(3):
        guess = int(input("Guess the number I'm thinking of in 3 tries or less! It's between 1 and 10:  "))
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        else:
            print("correct!")
            break

def main():
    printZero()
    guessNumber()

main()
