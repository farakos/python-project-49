#!/usr/bin/env python3

from brain_games import welcome
from brain_games import game_logics
from brain_games.games.calc import rules, get_question, get_correct_answer


def main():
    welcome.print_intro()
    name = welcome.get_name()
    welcome.welcome_user(name)
    game_logics.run_game(name, rules, get_question, get_correct_answer)


if __name__ == '__main__':
    main()
