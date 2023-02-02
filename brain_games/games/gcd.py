import random

task = 'Find the greatest common divisor of given numbers.'


def get_question():
    return (random.randint(1, 99), random.randint(1, 99))


def get_question_phrase(question):
    return f'{question[0]} {question[1]}'


def get_correct_answer(numbers):
    min_number = min(numbers[0], numbers[1])
    max_number = max(numbers[0], numbers[1])
    if max_number % min_number == 0:
        return str(min_number)
    for x in range(1, min_number // 2 + 1):
        if (min_number % x == 0) and (max_number % x == 0):
            result = x
    return str(result)
