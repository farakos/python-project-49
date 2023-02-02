import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    return random.randint(1, 997)


def get_question_phrase(question):
    return question


def get_correct_answer(number):
    for x in range(2, number // 2):
        if number % x == 0:
            return 'no'
    return 'yes'
