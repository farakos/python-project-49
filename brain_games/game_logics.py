import prompt


def run_game(task, get_question):
    from brain_games import welcome

    welcome.print_intro()
    name = welcome.get_name()
    welcome.welcome_user(name)
    print(task)

    answer_count = 0
    counts_to_win = 3

    while answer_count < counts_to_win:
        question = get_question()
        print(f'Question: {question[0]}')
        answer = prompt.string('Your answer: ')
        correct_answer = question[1]
        if answer == correct_answer:
            print('Correct!')
            answer_count += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
