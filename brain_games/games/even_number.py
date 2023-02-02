import random

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    return random.randint(0, 99)


def get_correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
