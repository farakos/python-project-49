import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    number = random.randint(1, 997)
    is_prime = 'yes'

    for x in range(2, number // 2):
        if number % x == 0:
            is_prime = 'no'
    return (number, is_prime)
