def letterGrade(percent_grade):
    if percent_grade >= 90:
        return "A"
    elif 80 <= percent_grade < 90:
        return "B"
    elif 70 <= percent_grade < 80:
        return "C"
    elif 60 <= percent_grade < 70:
        return "D"
    return "F"

def isPassing(percent_grade):
    letter = letterGrade(percent_grade)
    return letter == "A" or letter == "B" or letter == "C"

def main():
    grade = int(input("What grade do you want to check?  "))
    print(letterGrade(grade))
    print(isPassing(grade))

main()
