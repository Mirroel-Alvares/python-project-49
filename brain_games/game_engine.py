#!/usr/bin/env python3

from brain_games.cli import welcome_user
import prompt


def run_game(module):
    name = welcome_user()
    print(module.GAME_TASK)
    for round in range(3):
        question, correct_answer = module.get_question_correct_answer()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print('Correct!')

    print(f'Congratulations, {name}!')
