import random

task = 'Find the greatest common divisor of given numbers.'


def get_question():
    pair = (random.randint(1, 99), random.randint(1, 99))
    question = f'{pair[0]} {pair[1]}'

    min_number = min(pair[0], pair[1])
    max_number = max(pair[0], pair[1])

    if max_number % min_number == 0:
        answer = min_number
    else:
        for x in range(1, min_number // 2 + 1):
            if (min_number % x == 0) and (max_number % x == 0):
                answer = x

    return (question, str(answer))
