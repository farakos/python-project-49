#!/usr/bin/env python3

from brain_games import welcome
from brain_games import game_logics
from brain_games.games.even_number import rules
from brain_games.games.even_number import get_question
from brain_games.games.even_number import get_correct_answer


def main():
    welcome.print_intro()
    name = welcome.get_name()
    welcome.welcome_user(name)
    game_logics.run_game(name, rules, get_question, get_correct_answer,)


if __name__ == '__main__':
    main()
