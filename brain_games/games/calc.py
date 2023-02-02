import random

task = 'What is the result of the expression?'


def get_question():
    operations = ['+', '*']
    question = f'{random.randint(0, 10)} ' \
               f'{random.choice(operations)} ' \
               f'{random.randint(0, 10)}'
    operands = question.split()

    if operands[1] == '+':
        answer = int(operands[0]) + int(operands[2])
    else:
        answer = int(operands[0]) * int(operands[2])
    return (question, str(answer))
