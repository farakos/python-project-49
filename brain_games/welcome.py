def get_name():
    import prompt
    name = prompt.string('May I have your name? ')
    return name


def welcome_user(name):
    print(f'Hello, {name}!')