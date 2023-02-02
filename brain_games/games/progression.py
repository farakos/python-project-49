import random

task = 'What number is missing in the progression?'


def get_question():
    progression_len = random.randint(5, 15)
    progression = []
    start = random.randint(0, 20)
    step = random.randint(1, 10)

    for i in range(0, progression_len):
        progression.append(str(start))
        start += step

    hide_index = random.randint(0, progression_len - 1)
    missing_number = progression[hide_index]
    progression[hide_index] = '..'
    return (progression, missing_number)


def get_question_phrase(question):
    return ' '.join(question[0])


def get_correct_answer(question):
    return question[1]
