class WrongAnswerError(Exception):
    pass

class NoAnswerError(Exception):
    pass

try:
    food = input('What is your favorite food?  ')
    if food == '':
        raise NoAnswerError()
    if food != 'Pizza':
        raise WrongAnswerError()

except NoAnswerError:
    print('My favorite food is Pizza')

except WrongAnswerError:
    print('Wrong answer, buddy')
