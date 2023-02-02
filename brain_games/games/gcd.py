import random

task = 'Find the greatest common divisor of given numbers.'


def get_question():
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)

    for x in range(1, min(num_1, num_2) + 1):
        if (num_1 % x == 0) and (num_2 % x == 0):
            answer = x

    return (f'{num_1} {num_2}', str(answer))
