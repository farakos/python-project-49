#!/usr/bin/env python3

from brain_games import welcome
from brain_games import even_number


def main():
    print('Welcome to the Brain Games!')
    name = welcome.get_name()
    welcome.welcome_user(name)
    even_number.ask_number(name)


if __name__ == '__main__':
    main()
