def ask_number(name):
    import random
    import prompt

    def is_even(number):
        if number % 2 == 0:
            return 'yes'
        return 'no'

    print('Answer "yes" if the number is even, otherwise answer "no".')

    answer_count = 0

    while answer_count < 3:
        number = random.randint(0, 100)

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(number)
        if answer == correct_answer:
            print('Correct!')
            answer_count += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
