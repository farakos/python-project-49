import prompt


def run_game(name, rules, get_question, get_correct_answer):
    print(rules)

    answer_count = 0
    counts_to_win = 3

    while answer_count < counts_to_win:
        question = get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(question)
        if answer == correct_answer:
            print('Correct!')
            answer_count += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
