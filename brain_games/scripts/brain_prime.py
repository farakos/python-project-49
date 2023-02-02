#!/usr/bin/env python3

from brain_games import game_logics
from brain_games.games.prime_number import task
from brain_games.games.prime_number import get_question


def main():
    game_logics.run_game(task, get_question)


if __name__ == '__main__':
    main()
