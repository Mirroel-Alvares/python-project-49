#!/usr/bin/env python3

# from brain_games.cli import *
# from brain_games.cli import name
# from brain_games.scripts.brain_games import *

import prompt
from random import randint


def is_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1, 99)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if num % 2 == 0 and answer == 'yes':
            print('Correct!')
            i += 1
        elif num % 2 != 0 and answer == 'no':
            print('Correct!')
            i += 1
        else:
            if num % 2 == 0:
                print(
                  f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was 'yes'.\nLet's try again, {name}!"
                )
            else:
                print(
                  f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was 'no'.\nLet's try again, {name}!"
                )
            break
    if i == 3:
        print(f'Congratulations, {name}!')


def main():
    print(f'{"Welcome to the Brain Games!"}')
    is_even()


if __name__ == '__main__':
    main()
