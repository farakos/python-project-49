import random

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    number = random.randint(0, 99)

    if number % 2 == 0:
        is_even = 'yes'
    else:
        is_even = 'no'
    return (number, is_even)
