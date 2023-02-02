import random

task = 'Find the greatest common divisor of given numbers.'


def get_question():
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    min_number = min(num_1, num_2)
    max_number = max(num_1, num_2)

    if max_number % min_number == 0:
        answer = min_number
    else:
        for x in range(1, min_number // 2 + 1):
            if (min_number % x == 0) and (max_number % x == 0):
                answer = x

    return (f'{num_1} {num_2}', str(answer))
