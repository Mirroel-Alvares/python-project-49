#!/usr/bin/env python3

import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game_modules):
    name = welcome_user()
    print(game_modules.GAME_TASK)
    count = 0
    game_round = 3
    while count < game_round:
        question, correct_answer = game_modules.game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')
