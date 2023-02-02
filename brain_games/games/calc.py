import random

rules = 'What is the result of the expression?'


def get_question():
    operations = ['+', '*']
    return f'{random.randint(0, 20)} {random.choice(operations)} {random.randint(0, 20)}'


def get_correct_answer(expression):
    operands = expression.split()

    if operands[1] == '+':
        result = int(operands[0]) + int(operands[2])
    else:
        result = int(operands[0]) * int(operands[2])
    return str(result)