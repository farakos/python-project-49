import prompt


def print_intro():
    print('Welcome to the Brain Games!')


def get_name():
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(name):
    print(f'Hello, {name}!')
